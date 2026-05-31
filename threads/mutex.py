import threading
import time
from .pylogger import logger

class MultiThreadedStateUpdate():
    def __init__(self):
        self.state = 0
        self.lock = threading.Lock()
        self.switch = threading.Event()

    def updateState(self):
        while not self.switch.is_set():
            with self.lock:
                logger.info("Acquired lock, updating state")
                self.state += 1
                logger.info(f"State = {self.state}")
            logger.info("Releasing lock, going to sleep")
            time.sleep(2)
            logger.info(f"Latest state value (post sleep) = {self.state}")
            


MultiThreadedStateUpdateInstance = MultiThreadedStateUpdate()

threads: list[threading.Thread] = []
for _ in range(0, 10):
    _thread: threading.Thread = threading.Thread(target=MultiThreadedStateUpdateInstance.updateState)
    _thread.start()
    threads.append(_thread)

time.sleep(10)
logger.warning("Setting event kill switch to close threads")
MultiThreadedStateUpdateInstance.switch.set()

for thread in threads:
    thread.join()