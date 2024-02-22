from speech import speech_tr
import discord
from discord.ext import commands
import os, random
import requests
from googlesearch import search

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command('duck')
async def duck(ctx):
    await ctx.send("test")

@bot.command("googlesearch")
async def googlesearch(ctx, *search_msg: str):
    searchmessage = "".join(search_msg)
    for URL in search(searchmessage, stop=5):
        url = URL
        await ctx.message.author.send(str(url))
bot.run("MTIwNzc1MTAyMjIxOTYyNDQ2OQ.G-bREp.GXDcaPabl5b0w0XBzSGRlCyzpAVH0Cj3JDiHio")
