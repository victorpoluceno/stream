from stream.component import Component


class Spout(Component):

    def open(self, collector):
        self.collector = collector

    def next_tuple(self):
        raise NotImplementedError
