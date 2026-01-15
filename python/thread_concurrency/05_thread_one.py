import threading
import time

def boil_milk():
    print(f"{threading.current_thread().name} started boiling milk")
    time.sleep(2) 
    print(f"{threading.current_thread().name} finished boiling milk")
    
def toast_bread():
    print(f"{threading.current_thread().name} started toasting bread")
    time.sleep(3)  
    print(f"{threading.current_thread().name} finished toasting bread")


start = time.time()

milk_thread = threading.Thread(target = boil_milk, name="Milk-Thread")
bread_thread = threading.Thread(target = toast_bread, name="Bread-Thread")

milk_thread.start()
bread_thread.start()

milk_thread.join()
bread_thread.join()

end = time.time()
print(f"Total execution time: {end - start} seconds")