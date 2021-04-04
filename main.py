import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!박경배 ")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def 훈련병(ctx):
    await ctx.send('128번 훈련병 박경배!')


@bot.command()
async def 계급(ctx):
    await ctx.send('현재 저는 훈련병입니다!')


bot.run('')
