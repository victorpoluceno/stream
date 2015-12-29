from Queue import Queue
import threading

from xwing.client import Client
from xwing.server import Server


class Gateway(threading.Thread):

    def __init__(self, manager_address, identity, queue_in, queue_out):
        super(Gateway, self).__init__()
        self.manager_address = manager_address
        self.identity = identity
        self.queue_in, queue_out = queue_in, queue_out

    def run(self):
        server = Server(self.manager_address, self.identity)

        while True:
            value = server.recv()
            self.queue_in.put(value)

            try:
                value = self.queue_out.get(block=False)
            except Queue.Empty:
                continue

            #client = Client('localhost:4444', self.identity)
            #client.send(b'0', value)
