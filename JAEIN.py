import discord

client = discord.Client()


@client.event
async def on_ready():
    print("남탕대장 출근!")
    print(client.user.name)
    print(client.user.id)
    print("===========")
    print("이것은 조선관리인 봇의 클라이언트입니다")
    print("본 클라이언트의 저작권은 세콤에게 있습니다")
    print("현재 남탕관리인이 사용할수 있는 명령어는")
    print("!명령어,!변태순위 입니다")
    print("===========")

    await client.change_presence(game=discord.Game(name="북한이 먼저다", type=1))


@client.event
async def on_message(message):
    if message.author.bot:
        return None

    id = message.author.id
    channel = message.channel

    if message.content.startswith("!재이니한마디"):
        channel = message.channel
        embed = discord.Embed(
            title='크흠큼큼',
            description='어..궁민 여러분..',
            colour=discord.Colour.blue()
        )

        embed.set_footer(text='이상입다')
        embed.add_field(name='.', value='샤뢈이 먼줘다!', inline=False)
        embed.set_image(url="https://search.pstatic.net/common?type=a&size=120x150&quality=95&direct=true&src=http%3A%2F%2Fsstatic.naver.net%2Fpeople%2Fportrait%2F201611%2F20161122215734443.png")

        await client.send_message(channel, embed=embed)

client.run("NTkxOTU4NTMyNDcyMDQ1NTg2.XQ4Xdg.FRnJ-sGrYFC-e9RfXUrIGBrVqA0")
