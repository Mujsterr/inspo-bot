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
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.streaming, name = "inspiration"))

@client.command(aliases = ['I','ins'])
async def inspire(ctx):
    IMG_LINK = scraper.img_url_grabber()
    embed = discord.Embed(
        title = 'InspiroBot',
        description = 'You have been inspired!',
        colour = discord.Colour.from_rgb(127, 101, 164)
    )
    #emoji ="\N{THUMBS UP SIGN}"
    #Context.message.add_reaction(emoji)
    embed.set_image(url = IMG_LINK)
    await ctx.send(embed = embed)

    tz = timezone('US/Eastern')
    aiocron.crontab('0 15 * * *', func= inspire, tz = tz) 

client.run(TOKEN)
