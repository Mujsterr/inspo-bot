import os
import discord
import scraper
import asyncio

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
IMG_LINK = scraper.img_url_grabber()
 

client = discord.Client()

@client.event
async def on_message(message):
    if message.content == ">inpso":
        await message.channel.send("HellO!")

client.run(TOKEN)