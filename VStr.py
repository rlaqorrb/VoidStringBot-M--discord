import discord
import asyncio

client = discord.Client()

token = "ODE5ODQ3NjE2MDc0NDgxNzA2.YEsklw.kwi_WaD03U3xBivkPBJz_aXkpEI"

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')
    game = discord.Game('VoidString')
    await client.change_presence(status=discord.Status.online, activity=game)

intros = "```cs"
introf = "```"
intro1 = "#활동 목표" 
intro2 = "1.기본적인 컴퓨터 기술을 배우고 각자 필요한 각종 자격증 취득 및 대회참가활동"
intro3 = "1. 기본 컴퓨터 기술과 용어, 프로그램 언어를 배우고, 매년 말에 다같이 프로그램을 만든다. ➡ 한달에 한가지씩 배운다."
intro4 = "2. 각자 필요한 자격증을 취득한다."
intro5 = "3. 매달 마지막날 1시간동안 한달간 배운것을 정리하여 함께 토론하여 정리하는 시간을 가진다."
intro6 = "4. 여유가 있을 때엔 함께 대회참가를 한다."

@client.event
async def on_message(message):
    if message.content == "!도움":
        await message.channel.send("```\n명령어\n```\n```\n!활동내용\n!질문\n```\n```음악봇\n!help```")
    if message.content == "!활동내용":
        await message.channel.send(intros + "\n" + intro1 + "\n" + intro2 + "\n" + introf + "\n" + intros + "\n#활동내용\n" + intro3 + "\n" + intro4 + "\n" + intro5 + "\n" + intro6 + "\n" + introf)

client.run("ODE5ODQ3NjE2MDc0NDgxNzA2.YEsklw.kwi_WaD03U3xBivkPBJz_aXkpEI")
