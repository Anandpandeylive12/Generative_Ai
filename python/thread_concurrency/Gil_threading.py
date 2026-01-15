import threading
import time


def brew_chai():
    print(f"{threading.current_thread().name} started brewing chai")
    count = 0
    for _ in range(50000000):
        count += 1  
    print(f"{threading.current_thread().name} finished brewing chai")

thread_01 = threading.Thread(target=brew_chai, name="Thread-1")
thread_02 = threading.Thread(target=brew_chai, name="Thread-2")

start = time.time()
thread_01.start()
thread_02.start()

thread_01.join()
thread_02.join()
end = time.time()
print(f"Total time taken: {end - start:.2f} seconds")