import os
import discord
import scraper
import asyncio

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('.env')

TOKEN = os.environ.get("TOKEN")

intents = discord.Intents.all()
client = commands.Bot(command_prefix = ';',intents = intents)

@client.command(aliases = ['I','ins'])
async def inspire(ctx):
    IMG_LINK = scraper.img_url_grabber()
    embed = discord.Embed(
        title = 'You have been inspired!',
        colour = discord.Colour.from_rgb(135, 248, 239)
    )
    embed.set_image(url = IMG_LINK)
    await ctx.send(embed = embed)

client.run(TOKEN)
