"""
We learn the concept of blocking and non-blocking locks in Threads
Non-blocking doesn't just hold off the thread at the lock stage, else all your n-threads would be waiting on the lock
hogging up resources not doing anything else; so non-blocking allows the thread to be used elsewhere

"""

import time
from typing import List
from typing import Callable
from operator import call
from threading import Lock, Thread
from pylogger import logger

def taskA(lock: Lock, counter: int):
    logger.info(f"waiting to acquire lock")
    lock.acquire()
    logger.info(f"lock acquired")
    counter += 1
    time.sleep(2)
    lock.release()
    logger.info(f"lock released")
    

def taskB(lock: Lock, counter: int):
    """Blocking Lock for this task"""
    logger.info(f"waiting to acquire lock")
    lock.acquire()
    logger.info(f"lock acquired")
    counter += 1
    time.sleep(2)
    lock.release()
    logger.info(f"lock released")

def taskC(lock: Lock, counter: int):
    """Non-Blocking Lock for this task"""
    logger.info(f"waiting to acquire lock")
    while not lock.acquire(blocking=False):
        logger.info("Doing something else while lock isn't available")
        time.sleep(0.01)

    logger.info(f"lock acquired")
    counter += 1
    lock.release()
    logger.info(f"lock released")


if __name__ == "__main__":
    counter: int = 100
    lock: Lock = Lock()
    tasks: List[Callable] = [taskA, taskB, taskC]
    _threads = [Thread(target=task, args=(lock,counter)) for task in tasks]
    for thread in _threads: thread.start()
    for thread in _threads: thread.join()

