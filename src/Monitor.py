from threading import Semaphore, Lock
from time import sleep


class Monitor:
    def __init__(self, size):
        self.empty_semaphore = Semaphore(size)
        self.full_semaphore = Semaphore(0)
        self.mutex = Lock()
        self.buffer = []
        self.size = size

    def insert(self, item):
        if len(self.buffer) == self.size:
            self.empty_semaphore.acquire()
        
        self.mutex.acquire()

        self.buffer.append(item)
        print(self.buffer)
        
        self.mutex.release()

        if len(self.buffer) == 1:
            self.full_semaphore.release()

    def remove(self):
        if len(self.buffer) == 0:
            self.full_semaphore.acquire()

        self.mutex.acquire()

        item = self.buffer.pop(0)
        print(self.buffer)

        self.mutex.release()

        if len(self.buffer) == self.size - 1:
            self.empty_semaphore.release()
        
        return item
