from threading import Semaphore, Lock


class ProducerConsumer:
    def __init__(self, size):
        self.empty_semaphore = Semaphore(size)
        self.full_semaphore = Semaphore(0)
        self.mutex = Lock()
        self.buffer = []
        self.size = size

    def insert(self, item):
        self.empty_semaphore.acquire()
        self.mutex.acquire()

        self.buffer.append(item)
        print(self.buffer)
        
        self.mutex.release()
        self.full_semaphore.release()

    def remove(self):
        self.full_semaphore.acquire()
        self.mutex.acquire()

        item = self.buffer.pop(0)
        print(self.buffer)

        self.mutex.release()
        self.empty_semaphore.release()
        
        return item
