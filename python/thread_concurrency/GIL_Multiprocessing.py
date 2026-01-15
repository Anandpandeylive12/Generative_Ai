from multiprocessing import Process
import time

def crunch_number():
    print(f"starting the count process")
    count = 0
    for i in range(50000000):
        count += 1
    print(f"counting process finished")
    
if __name__ == "__main__":
    start = time.time()

    p1=Process(target=crunch_number)
    p2=Process(target=crunch_number)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end= time.time()

    print(f"the entire process took {end - start} seconds")