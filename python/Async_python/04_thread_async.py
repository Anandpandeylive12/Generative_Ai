import asyncio
import time

from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print("chechking {items} in store ... ..... ... ")
    time.sleep(3) #Bloking operation
    return f"{item} are in stock"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Masala Chai")
        print(result)
        
asyncio.run(main())