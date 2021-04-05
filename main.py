import discord
import random
import datetime
import os
import random

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
    discharge_2022 = datetime.datetime(2021, 5, 4,)
    days = (discharge_2022 - datetime.datetime.now()).days

    if days >= 0:
        return days
    else:
        return str("이미 입대했습니다.")


def days_until_enlist_hour():
    dateformat = "%Y-%m-%d %H:%M:%S"
    start_datetime = datetime.datetime.now()
    end_datetime = "2021-05-04 00:00:00"

    datetime_convert1 = datetime.datetime.strptime(start_datetime, dateformat)
    datetime_convert2 = datetime.datetime.strptime(end_datetime, dateformat)

    days = (datetime_convert2 - datetime_convert1).seconds/3600

    return days


def ext_milText():
    with open("ext_mil.txt") as f:
        answer = random.randint(0, 100)
        data = f.readlines()[answer]
        return data


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def 도움말(ctx):
    embed = discord.Embed(title="박경배 도움말",
                          description="봇 서버가 켜지지 않으면 동작하지 않습니다. 봇의 온/오프라인 상태를 확인할 수 있습니다.",
                          color=0x24872d)
    embed.add_field(name="!박경배 도움말", value="도움말을 표시합니다.", inline=False)
    embed.add_field(name="!박경배 입대일", value="입대일과 그 날까지 며칠 남았는지 계산하여 보여줍니다.", inline=False)
    embed.add_field(name="!박경배 전역일", value="전역일과 그 날까지 며칠 남았는지 계산하여 보여줍니다.", inline=False)
    embed.add_field(name="!박경배 계급", value="현재 박경배의 계급과 앞으로 진급할 진급 날짜를 리스트로 보여줍니다.", inline=False)
    embed.add_field(name="!박경배 군생활어록", value="군생활 하는 동안 필요한 어록을 랜덤으로 보여줍니다. 총 100개 수", inline=False)
    embed.set_footer(text="-v1.0.0 / 20210405 Latest Update")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/827970631588511776/828345600830341150/unnamed.png")
    await ctx.channel.send("안녕하세요, Hakbong2_bot입니다. 저를 사용하는 방법에 대해서 설명하겠습니다.", embed=embed)


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
    embed.set_footer(text="-도움이 필요할 땐, 국방헬프콜 ☎1303")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/827970631588511776/828345600830341150/unnamed.png")
    await ctx.channel.send("안녕하세요, Hakbong2_bot입니다. 저의 계급을 알려드리겠습니다.", embed=embed)


@bot.command()
async def 입대일(ctx):
    embed = discord.Embed(title="집떠나와 열차타고 훈련소로 가는날..까지 며칠이 남았을까?",
                          description="그 날까지 __**"+str(days_until_enlist()) +
                                      "**__일 남았다..! \n 입대일: 2021년 5월 4일",
                          color=0x24872d)
    embed.set_footer(text="-도움이 필요할 땐, 국방헬프콜 ☎1303")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/827970631588511776/828345600830341150/unnamed.png")
    await ctx.channel.send("안녕하세요, Hakbong2_bot입니다. 저는 곧 입대합니다.", embed=embed)


@bot.command()
async def 전역일(ctx):
    embed = discord.Embed(title="박경배, 그는 언제 전역하는가?",
                          description="충성! 제 전역일은 **2022년 11월 3일**입니다. "
                                      "\n 총 __**"+str(days_until_discharge())+"**__일 남았습니다....", color=0x24872d)
    embed.set_footer(text="-도움이 필요할 땐, 국방헬프콜 ☎1303")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/827970631588511776/828345600830341150/unnamed.png")
    await ctx.channel.send("안녕하세요, Hakbong2_bot입니다. 저의 전역일을 계산해 보겠습니다.", embed=embed)


@bot.command()
async def 군생활어록(ctx):
    embed = discord.Embed(title="많은 사람들이 남긴 군생활 어록",
                          description=str(ext_milText()), color=0x24872d)
    embed.set_footer(text="-도움이 필요할 땐, 국방헬프콜 ☎1303")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/827970631588511776/828345600830341150/unnamed.png")
    await ctx.channel.send("안녕하세요, Hakbong2_bot입니다. 총 100개의 어록 중 하나를 뽑아봤습니다..", embed=embed)

bot.run(DISCORD_TOKEN)
