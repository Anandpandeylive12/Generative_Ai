import threading
import time


def prepare_chai(Type_,wait_time):
    print(f"{threading.current_thread().name} started preparing {Type_} chai")
    time.sleep(wait_time)
    print(f"{threading.current_thread().name} finished preparing {Type_} chai") 
    
t1 = threading.Thread(target=prepare_chai,args=("Masala",5))
t2 = threading.Thread(target=prepare_chai,args=("Ginger",2))

t1.start()
t2.start()
t1.join()
t2.join()

print("Both types of chai are ready!")