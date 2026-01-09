from multiprocessing import Process
import time

def brew_chai(name):
    print(f"start of {name} brewing chai")
    time.sleep(3)
    print(f"End of {name} brewing chai")
    
if __name__ == '__main__':
    chai_makers = [
        Process(target=brew_chai, args=(f"ChaiMaker-{i}",))
        for i in range(3)
    ]
     #starting processes
    for p in chai_makers:
         p.start()  
     #waiting for processes to complete
    for p in chai_makers:
         p.join()
     
     #final message
    print("All chai brewed.")