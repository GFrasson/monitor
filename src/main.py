from threading import Thread
from Monitor import Monitor


def produce(monitor, item):
    # while True:
        monitor.insert(item)


def consume(monitor):
    # while True:
        monitor.remove()


if __name__ == '__main__':
    monitor = Monitor(5)

    # producer_threads = []
    # consumer_threads = []
    threads = []
    
    producer_threads_amount = 10
    consumer_threads_amount = 10

    for i in range(0, producer_threads_amount):
        thread = Thread(target=produce, args=(monitor, i))
        threads.append(thread)

    for i in range(0, consumer_threads_amount):
        thread = Thread(target=consume, args=(monitor,))
        threads.append(thread)
    
    for thread in threads:
        thread.start()
