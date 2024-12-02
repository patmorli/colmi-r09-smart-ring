import asyncio
from bleak import discover

async def scan():
    devices = await discover()
    for d in devices:
        print(f"{d.name} ({d.address})")

asyncio.run(scan()) 