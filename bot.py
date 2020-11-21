import os
import discord
import scraper
import asyncio

from discord.ext import commands



TOKEN = os.environ.get('TOKEN')
IMG_LINK = scraper.img_url_grabber()
 

client = discord.Client()


@client.event
async def on_message(message):
    if message.content == ">inpso":
        await message.channel.send("HellO!")

client.run(TOKEN)