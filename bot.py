import os
import discord
import scraper

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
IMG_LINK = scraper.img_url_grabber()
client = discord.Client()

client.run(TOKEN)