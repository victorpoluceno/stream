import uuid
from Queue import Queue

from stream.task.gateway import Gateway
from stream.task.executor import Executor


class Instance:

    def __init__(self, module, klass, manager_address, identity):
        self.module = module
        self.klass = klass
        self.manager_address = manager_address
        self.identity = uuid.uuid1() if identity is None else identity

    def run(self):
        component = make_component(self.module, self.klass)
        queue_in, queue_out = Queue(), Queue()

        executor = Executor(component, queue_in, queue_out)
        executor.start()

        gateway = Gateway(self.manager_address, self.identity, queue_in,
                          queue_out)
        gateway.start()

        executor.join()


def make_component(module, klass):
    component = __import__(module, globals(), locals(), [klass], 0)
    return getattr(component, klass)
