import interactions
from datastore.imports import DatabaseClient
bot = interactions.Client(token="OTU4ODEwMjI5NTI3Njc5MDA2.YkSvnA.sUWJy5GYgV7mtk5LY5LjuEh86Fc")

db = DatabaseClient(universeId=1, token=".", ROBLOSECURITY="_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|")

@bot.event
async def on_ready():
    await db.set_data(datastore="Test", key="Test", data={"Hello": "World"})
    await db.set_data(datastore="Test", key="Test/Hello", data="World1")
    p = await db.get_keys(datastore="Test", limit=100)
    print(p)

bot.start()
