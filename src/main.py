from threading import Thread
from Monitor import ProducerConsumer


class Program:
    def __init__(self, producer_consumer_monitor) -> None:
        self.producer_consumer_monitor = producer_consumer_monitor

    def produce(self, item):
        while True:
            self.producer_consumer_monitor.insert(item)

    def consume(self):
        while True:
            self.producer_consumer_monitor.remove()


if __name__ == '__main__':
    buffer_size = 5
    producer_consumer_monitor = ProducerConsumer(buffer_size)
    program = Program(producer_consumer_monitor)

    threads = []
    
    producer_threads_amount = 3
    consumer_threads_amount = 3

    for i in range(0, producer_threads_amount):
        thread = Thread(target=program.produce, args=(i,))
        threads.append(thread)

    for i in range(0, consumer_threads_amount):
        thread = Thread(target=program.consume)
        threads.append(thread)
    
    for thread in threads:
        thread.start()
