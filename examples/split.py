from stream.component import Bolt


class Split(Bolt):

    def execute(self, value):
        for word in value.split():
            self.emit(word)
