from multiprocessing import Process, Queue

def prepare_chai(queue):
    queue.put("Masala Chai is ready!")
    
if __name__ == "__main__":
    queue = Queue()
    process = Process(target=prepare_chai, args=(queue,))
    process.start()
    process.join()
    
    message = queue.get()
    print(message)