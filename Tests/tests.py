from imports import DatabaseClient
import asyncio

async def main_def():
    client = DatabaseClient(universeId=3298669091, token="0bI1AKfEIEe9sDlo1DDI5vg7v55/OTTDG9pcib8f5HwZCOLI")
    await client.get_datastores()
asyncio.run(main_def())