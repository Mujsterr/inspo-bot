import os
import discord
import scraper
import asyncio

from dotenv import load_dotenv

load_dotenv('.env')

TOKEN = os.environ.get("TOKEN")

intents = discord.Intents.all()
client = discord.Client(intents =intents)

@client.event
async def on_message(message):
    if message.content == ">inspo":
        channel = message.channel
        await channel.send(scraper.img_url_grabber())

client.run(TOKEN)
