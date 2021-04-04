import discord
import random
import datetime
import os

from discord.ext import commands
from dotenv import load_dotenv

token = open("bot_token", "r").readline()

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!박경배 ")
now = datetime.datetime.now()


def days_until_discharge():
    discharge_2022 = datetime.datetime(2022, 11, 3)
    days = (discharge_2022 - datetime.datetime.now()).days
    return days


def days_until_enlist():
    discharge_2022 = datetime.datetime(2021, 5, 4)
    days = (discharge_2022 - datetime.datetime.now()).days

    if days >= 0:
        return days
    else:
        return str("이미 입대했습니다.")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def 도움말(ctx):
    await ctx.send('현재 저는 훈련병입니다!')


@bot.command()
async def 훈련병(ctx):
    await ctx.send('128번 훈련병 박경배!')


@bot.command()
async def 계급(ctx):
    classes = "__**민간인**__"
    classes_point = 0
    if days_until_discharge() > 548:
        classes = "__**곧 군대감 ㅋㅋ**__"
    elif 521 <= days_until_discharge() <= 548:
        classes = "__**훈련병**__"
    elif 491 <= days_until_discharge() <= 547:
        classes = "__**이등병**__"
    elif 307 <= days_until_discharge() <= 490:
        classes = "__**일등병**__"
    elif 459 <= days_until_discharge() <= 126:
        classes = "__**상등병**__"
    elif 125 <= days_until_discharge() <= 1:
        classes = "__**병장**__"

    embed = discord.Embed(title="군인 박경배, 그의 계급을 알아보자.", description="충성! 제 계급은 "+str(classes)+"입니다!!", color=0x24872d)
    embed.add_field(name="박경배's 군생활 계급예정표", value="육군은 진급하는 달 1일에 진급을 원칙으로 함.", inline=False)
    embed.add_field(name="이등병", value="ㅋㅋ입대하자마자 이등병이지 뭐. tip) 훈련병도 이등병임, 총 2호봉", inline=False)
    embed.add_field(name="일등병", value="21년 7월 1일 일등병 1호봉으로 진급, 총 6호봉.", inline=False)
    embed.add_field(name="상등병", value="22년 1월 1일 상등병 1호봉으로 진급, 총 6호봉.", inline=False)
    embed.add_field(name="병장", value="22년 7월 1일 병장 1호봉으로 진급, 총 4호봉", inline=False)
    embed.set_footer(text="-걸리지 않은 가라는 가라가 아니다.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/827970631588511776/828345600830341150/unnamed.png")
    await ctx.channel.send("안녕하세요, Hakbong2_bot입니다. 저의 전역일을 계산해 보겠습니다.", embed=embed)


@bot.command()
async def 입대(ctx):
    embed = discord.Embed(title="집떠나와 열차타고 훈련소로 가는날..까지 며칠이 남았을까?", description="그 날까지 __**"+str(days_until_enlist()) + "**__일 남았다..!",
                          color=0x24872d)
    embed.set_footer(text="-시계는 거꾸로 매달아놔도 움직인다.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/827970631588511776/828345600830341150/unnamed.png")
    await ctx.channel.send("안녕하세요, Hakbong2_bot입니다. 저는 곧 입대합니다.", embed=embed)


@bot.command()
async def 전역(ctx):
    embed = discord.Embed(title="박경배, 그는 언제 전역하는가?", description="충성! "+str(days_until_discharge())+"일 남았습니다....", color=0x24872d)
    embed.set_footer(text="-시계는 거꾸로 매달아놔도 움직인다.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/827970631588511776/828345600830341150/unnamed.png")
    await ctx.channel.send("안녕하세요, Hakbong2_bot입니다. 저의 전역일을 계산해 보겠습니다.", embed=embed)



bot.run(DISCORD_TOKEN)
