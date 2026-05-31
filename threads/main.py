import threading
import time


start = time.perf_counter()

def something(seconds: int = 2) -> None:
    print(f"sleeping for {seconds} second(s)")
    time.sleep(seconds)
    print("Finished sleeping ...")

threads: list[threading.Thread] = []
for _ in range(0, 10):
    _thread: threading.Thread = threading.Thread(target=something)
    _thread.start()
    threads.append(_thread)

for thread in threads:
    thread.join()

print(f"Total time taken: {time.perf_counter() - start}")