import os
import discord
import scraper
import asyncio
import aiocron

from pytz import timezone
from discord.ext import commands 
from discord.utils import find
from dotenv import load_dotenv

load_dotenv('.env')

TOKEN = os.environ.get("TOKEN")
INV_LINK = os.environ.get("INV_LINK")

intents = discord.Intents.all()
client = commands.Bot(command_prefix = ';', intents = intents, help_command = None )

@client.event
async def on_guild_join(guild):
    embed = discord.Embed(
                description = 'Say hello to InspiroBot!, type `;help` to get started.',
                colour = discord.Colour.from_rgb(127, 101, 164)
                )
    embed.set_author(name = 'InspiroBot', icon_url = 'https://media.discordapp.net/attachments/770804416252870677/782629864917565440/unknown.png?width=771&height=609')
    embed.set_thumbnail(url = 'https://discord.com/assets/df7ba0f4020ca70048a0226d1dfa73f6.svg')
    
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send(embed = embed)
        
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.playing, name = ";help"))

@client.command()
async def help(ctx):
  embed = discord.Embed(
        description = 'InspiroBot graces your Discord server by sending motivational humorous quotes from `inspirobot.me`.\n\n Use `;I` `;ins` or `;inspire` to get started.\n\n InspiroBot will greet you with a \U0001F44D and some nonsensical inspiration!\n',
        colour = discord.Colour.from_rgb(127, 101, 164)
    )
  embed.set_author(name = 'InspiroBot - Help is here!', icon_url = 'https://media.discordapp.net/attachments/770804416252870677/782629864917565440/unknown.png?width=771&height=609')
  embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/778770571130568704/782682275711549470/PinClipart.com_question-mark-clipart_5294773.png?width=609&height=609')
  embed.add_field(name = 'Add to discord', value = 'InspiroBot can be added to your server too! ' + INV_LINK)
  await ctx.send(embed = embed)
    
@client.command(aliases = ['I','ins'])
@commands.cooldown(3, 5, commands.BucketType.guild)
async def inspire(ctx):
    await ctx.message.add_reaction("\U0001F44D")
    
    IMG_LINK = scraper.img_url_grabber()
    embed = discord.Embed(
        description = '`You have been inspired!`',
        colour = discord.Colour.from_rgb(127, 101, 164)
    )
    embed.set_image(url = IMG_LINK)
    embed.set_author(name = 'InspiroBot', icon_url = 'https://media.discordapp.net/attachments/770804416252870677/782629864917565440/unknown.png?width=771&height=609')
    embed.set_thumbnail(url ='https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Quotation_marks.svg/512px-Quotation_marks.svg.png')
    await ctx.send(embed = embed)
    await ctx.message.add_reaction("\U00002705")

@client.event
async def is_on_cooldown(ctx):
    embed = discord.Embed(
        description ="Command on cooldown, Please try again later",
        colour = discord.Colour.from_rgb(127, 101, 164)
    )
    embed.set_author(name = 'InspiroBot', icon_url = 'https://media.discordapp.net/attachments/770804416252870677/782629864917565440/unknown.png?width=771&height=609')
    await ctx.send(embed = embed)

client.run(TOKEN)
