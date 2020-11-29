import os
import discord
import scraper
import asyncio
import aiocron

from pytz import timezone
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('.env')

TOKEN = os.environ.get("TOKEN")

intents = discord.Intents.all()
client = commands.Bot(command_prefix = ';', intents = intents)

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.playing, name = "inspiration"))

@client.command(aliases = ['I','ins'])
async def inspire(ctx):
    IMG_LINK = scraper.img_url_grabber()
    embed = discord.Embed(
        title = 'InspiroBot',
        description = 'You have been inspired!',
        colour = discord.Colour.from_rgb(127, 101, 164)
    )
    embed.set_image(url = IMG_LINK)

    await ctx.send(embed = embed)

@client.event
async def reaction(message):
    if message in (';I', ';ins'):
            emoji ="👍"
    await message.add_reaction(message, emoji) 
    
client.run(TOKEN)
