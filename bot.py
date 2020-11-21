import os
import discord
import scraper
import asyncio

from discord.ext import commands


TOKEN = os.environ.get("TOKEN")
#IMG_LINK = scraper.img_url_grabber()
client = commands.Bot(command_prefix= '>')

client = discord.Client()


@client.event
async def on_ready():
    print("Hello!")


@client.event
async def on_message(message):
    if message.content == ">inpso":
        await message.channel.send("Hello!")

client.run(TOKEN)
