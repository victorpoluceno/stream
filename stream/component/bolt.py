from stream.component import Component


class Bolt(Component):

    def prepare(self, collector):
        self.collector = collector

    def execute(self, value):
        raise NotImplementedError
