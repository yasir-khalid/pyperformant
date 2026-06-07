from time import sleep
from concurrent.futures import ThreadPoolExecutor
import time

sleep
start = time.perf_counter()

def something(seconds: int = 2) -> None:
    print(f"sleeping for {seconds} second(s)")
    time.sleep(seconds)
    print("Finished sleeping ...")
    return seconds


with ThreadPoolExecutor() as executor:
    _future1 = executor.submit(something, 3)
    _future2 = executor.submit(something, 4)

    print(f"{_future1} return value: {_future1.result()}")
    print(f"{_future2} return value: {_future2.result()}")


with ThreadPoolExecutor() as executor:
    _runtime = [5,4,3,2,1]
    results = executor.map(something, _runtime)
    print(results)

    for result in results:
        print(result)



