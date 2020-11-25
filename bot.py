import os
import discord
import scraper
import asyncio

from dotenv import load_dotenv

load_dotenv('.env')

TOKEN = os.environ.get("TOKEN")
IMG_LINK = scraper.img_url_grabber()

intents = discord.Intents.all()
client = discord.Client(intents =intents)

@client.event
async def on_message(message):
    if message.content == ">inspo":
        channel = message.channel
        await channel.send(IMG_LINK)

client.run(TOKEN)
