from stream.component.spout import Spout


class Emit(Spout):

    def next_tuple(self):
        self.emit('Hello world!')
