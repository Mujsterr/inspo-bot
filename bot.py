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
    embed = discord.Embed(
        title = 'You have been inspired!',
        description = scraper.img_url_grabber(),
        colour = discord.Colour.blurple()
    )
    await ctx.send(embed = embed)

client.run(TOKEN)
