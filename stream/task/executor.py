import time
import threading

from stream.component.spout import Spout


def get_impl(component):
    if issubclass(component, Spout):
        return SpoutExecutor()

    return BoltExecutor()


class Executor(threading.Thread):

    def __init__(self, component, queue_in, queue_out):
        super(Executor, self).__init__()

        self.component = component
        self.queue_in, self.queue_out = queue_in, queue_out

        self.impl = get_impl(component)
        self.initialize()

    def initialize(self):
        collector = Collector(self.queue_out)
        self.impl.initialize(self.component, collector)

    def run(self):
        self.impl.run(self.queue_in, self.queue_out)


class BoltExecutor:

    def initialize(self, component, collector):
        self.component = component()
        self.component.prepare(collector)

    def run(self, queue_in, queue_out):
        while True:
            value = queue_in.get()
            self.component.execute(value)
            time.sleep(0.1)


class SpoutExecutor:

    def initialize(self, component, collector):
        self.component = component()
        self.component.open(collector)

    def run(self, queue_in, queue_out):
        while True:
            self.component.next_tuple()
            time.sleep(0.1)


class Collector:

    def __init__(self, queue_out):
        self.queue_out = queue_out

    def emit(self, value):
        self.queue_out.put(value)
