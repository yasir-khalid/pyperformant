"""
Highlights that if threads were to Truly start at the same time 
Reflective using Barrier concept, then the lock acquiring my threads is non-deterministic,
and hard to predict

Compared to when you just do a:
[thread.start() for thread in threads]
Here there might be a microseconds difference between n[0] vs n[1] thread, hence you see deterministic sequence
"""

import threading, time
from collections import Counter
from pylogger import logger


def make_worker(name, results):
    def worker(lock, barrier):
        logger.info("Waiting upto barrier entry")
        barrier.wait()  # release all threads simultaneously
        lock.acquire()
        logger.info("Acquired lock")
        results.append(name)
        time.sleep(0.001)
        lock.release()
        logger.info("Release lock")
    return worker

wins_first = Counter()
for trial in range(200):
    lock = threading.Lock()
    results = []
    names = [f"T{i}" for i in range(10)]
    barrier = threading.Barrier(len(names))
    threads = [threading.Thread(target=make_worker(n, results), args=(lock, barrier)) for n in names]
    for t in threads: t.start()
    for t in threads: t.join()
    wins_first[results[0]] += 1

print(wins_first)