import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} が起動しました")

@bot.command()
async def hello(ctx):
    await ctx.send("こんにちは！")

bot.run(os.getenv("TOKEN"))
