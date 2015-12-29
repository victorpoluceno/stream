class Component:

    def emit(self, *args, **kwargs):
        self.collector.emit(*args, **kwargs)
