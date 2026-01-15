import threading
import time
import requests
 
 
def download(url):
    print(f"{threading.current_thread().name} started downloading from {url}")
    response = requests.get(url)
    print(f"Finished downloading {len(response.content)} bytes from {url} of size:{len(response.content)} bytes")
    
urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = []
for url in urls:
    thread= threading.Thread(target = download , args=(url,))
    thread.start()
    threads.append(thread)
    
for thread in threads:
    thread.join()
    
end = time.time()
print(f"Total download time: {end - start:.2f} seconds")