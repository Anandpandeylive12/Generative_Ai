import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"taking order for table {i}")
        time.sleep(2)

def brew_chai():
     for i in range(1,4):
        print(f"brewing chai for table {i}")
        time.sleep(3)
        
#creating threads
order_thread = threading.Thread(target=take_orders).start()
brew_thread = threading.Thread(target=brew_chai).start()

#waiting for threads to complete
order_thread.join()
brew_thread.join()

print("All orders taken and chai brewed.")