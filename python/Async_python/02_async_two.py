import asyncio
import time

async def brew(name):
    print (f"brewing {name} chai ...")
    await asyncio.sleep(3)
    # time.sleep(3)
    print (f"{name} chai is ready!")
    
async def main():
    await asyncio.gather(
        brew("Masala"),
        brew("Ginger") ,
        brew("Lemon")
    )
    
asyncio.run(main())