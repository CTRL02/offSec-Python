import threading
import queue
import time


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


class WorkerThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        print("In WorkerThread")
        while True:
            task_info = self.queue.get()
            task_id = task_info[0]
            if task_id == 'add':
                result = add(task_info[1], task_info[2])
                print("Result of addition:", result)
            elif task_id == 'multiply':
                result = multiply(task_info[1], task_info[2])
                print("Result of multiplication:", result)
            elif task_id == 'print':
                print(task_info[1])
            else:
                print("Unknown task:", task_id)
            self.queue.task_done()


queue = queue.Queue()

# tasks to be performed by each thread concurrently
tasks = [
    ('add', 2, 3),
    ('multiply', 4, 5),
    ('print', Philo is Here!')
]

for i in range(5):
    print("Creating WorkerThread : %d" % i)
    worker = WorkerThread(queue)
    worker.setDaemon(True)
    worker.start()
    print("WorkerThread %d Created! " % i)

# so project only terminate when all threads finish executing
for task in tasks:
    queue.put(task)

queue.join()
