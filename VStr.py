import discord
import asyncio
import os

client = discord.Client()



@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')
    game = discord.Game('!도움')
    await client.change_presence(status=discord.Status.online, activity=game)

intros = "```cs"
introf = "```"
intro1 = "#활동 목표" 
intro2 = "1.기본적인 컴퓨터 기술을 배우고 각자 필요한 각종 자격증 취득 및 대회참가활동"
intro3 = "1. 기본 컴퓨터 기술과 용어, 프로그램 언어를 배우고, 매년 말에 다같이 프로그램을 만든다. ➡ 한달에 한가지씩 배운다."
intro4 = "2. 각자 필요한 자격증을 취득한다."
intro5 = "3. 매달 마지막날 1시간동안 한달간 배운것을 정리하여 함께 토론하여 정리하는 시간을 가진다."
intro6 = "4. 여유가 있을 때엔 함께 대회참가를 한다."
director = "부장(조윤성)"
leader = "대장(유가은)"
members = "```cs\n#1학년\n1. 10128 최의경\n2. 10203 김나영\n3. 10220 이현주\n4. 10309 김세은\n5. 10519 유가은[대장]\n6. 10608 김봉준\n7. 10609 김신후\n8. 10716 신유성\n9. 10822 이영준\n10. 10905 김민수\n11. 10907 김성욱\n12. 10913 두지훈\n13. 10914 문민성\n14. 10919 박준영\n15. 10920 배태환\n16. 10928 조윤성[부장]\n17. 11005 권해찬\n18. 11006 김건하\n19. 11011 김백규\n20. 11015 박진석\n21. 11016 신성훈```"
announcement2 = """
2021/04/07(수)/6교시
```fix
온라인 수업 2차시 영상```
```ini
[파이썬 기초 강의]```

https://www.youtube.com/watch?v=yytWGELNeOI

https://www.youtube.com/watch?v=I2yWGzxKKZg&list=WL&index=64
"""

@client.event
async def on_message(message):
    if message.content == "!도움":
        await message.channel.send("```ini\n[명령어]\n```\n```fix\n!활동내용\n!질문\n!부원명단```\n```fix\n음악봇\n!help```")
    if message.content == "!활동내용":
        await message.channel.send(intros + "\n" + intro1 + "\n" + intro2 + "\n" + introf + "\n" + intros + "\n#활동내용\n" + intro3 + "\n" + intro4 + "\n" + intro5 + "\n" + intro6 + "\n" + introf)
    if message.content == "!질문":
        await message.channel.send(director + "," + leader + "에게 문의")
    if message.content == "!부원명단":
        await message.channel.send(members)
    if message.content == "?":
        await message.channel.send("??")
    if message.content == "수학":
        await message.channel.send("tlqkf")
        await message.channel.send("тپ발")
        await message.channel.send("عپصمل")
        await message.channel.send("тќљчг")
    if message.content == "배고파":
        await message.channel.send("나도")
    if message.channel.send("공지"):
        await message.channel.send(announcement2)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
