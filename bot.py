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
client = commands.Bot(command_prefix = ';', intents = intents, help_command = None )


@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.playing, name = ";help"))

@client.command()
async def help(ctx):
  embed = discord.Embed(
        title = 'InspiroBot - Help is here!',
        description = 'InspiroBot graces your Discord server by sending motivational humorous quotes from `inspirobot.me`.\n\n Use `;I` `;ins` or `;inspire` to get started.\n\n InspiroBot will greet you with a \U0001F44D and some nonsensical inspiration!',
        colour = discord.Colour.from_rgb(127, 101, 164)
    )
  embed.add_field(name = 'Add to discord', value = 'InspiroBot can be added to your server too! [Click here to invite.](https://discord.com/api/oauth2/authorize?client_id=773097512499150849&permissions=11344&scope=bot)')
  await ctx.send(embed = embed)
    
@client.command(aliases = ['I','ins'])
async def inspire(ctx):
    await ctx.message.add_reaction("\U0001F44D")
    
    IMG_LINK = scraper.img_url_grabber()
    embed = discord.Embed(
        title = 'InspiroBot',
        description = '`You have been inspired!`',
        colour = discord.Colour.from_rgb(127, 101, 164)
    )
    embed.set_image(url = IMG_LINK)
    
    await ctx.send(embed = embed)
    await ctx.message.add_reaction("\U00002705")
    
client.run(TOKEN)
