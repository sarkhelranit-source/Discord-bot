import nextcord
from nextcord.ext import commands
from nextcord.ui import View
import random
import requests
from aiohttp import request
import asyncio
import pyjokes
import json
import datetime
import os
import youtube_dl
from webserver import keep_alive


def get_quotes():
    responses = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(responses.text)
    quote = json_data[0]['q'] + "\n -" + json_data[0]['a']

    return(quote)


bot = commands.Bot(command_prefix="!")


@bot.event
async def on_member_remove(ctx, member: nextcord.Member):
    await ctx.send(f"{member.name} just left the server😥... See you again my friend👋")


@bot.command()
async def ping(ctx):
    await ctx.send(f"Hey there! what's up\nHere is the current latency: {round(bot.latency * 1000)}ms")


@bot.command(aliases=["Q"])
async def _Q(ctx, *, question):
    responses = ["It is certain", "It is decidely so", "Without a doubt", "Yes - definately", "You may rely on it", "As I see it, yes",
                 "Most likely", "Yes", "Signs point to yes", "Don't count on it", "My reply is no", "My sources say no", "Very doubtful", "I don't think so"]
    await ctx.send(f"{random.choice(responses)}")


@bot.command()
async def choose(ctx, *, message):
    options = ["I chose the first one", "Um.. the first one",
               "Second one.. ig", "I chose the second one"]
    nope = ["Hey are u the guy who gets 96% chutiyarate tomorrow",
            f'''{ctx.author.name} needs some attention. plss co-operate everybody''', '''right command but wrong user. sorry noob''', '''Don't you think that you'll screw up''']

    if ctx.author.name == "Professor Unicorn":
        await ctx.send(random.choice(nope))
    else:
        await ctx.send(random.choice(options))


@bot.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    if (amount == 1):
        await ctx.send(f"{amount} message is deleted")
    elif(amount > 1):
        await ctx.send(f"{amount} messages got deleted")
    else:
        await ctx.send("DON'T ACT LIKE A DUMB😑")


@bot.command()
async def joke(ctx):
    url = "https://some-random-api.ml/joke"

    async with request("GET", url) as response:
        if response.status == 200:
            data = await response.json()
            await ctx.send(data["joke"])
        else:
            await ctx.send(f"Api Request Failed due to {response.status} error")


@bot.command()
async def whois(ctx, member: nextcord.Member):
    roles = [role for role in member.roles]

    emb = nextcord.Embed(title=f"{member.mention}", color=member.color)
    emb.set_author(
        name=f"{member.name}{member.discriminator}", icon_url=member.avatar_url)
    emb.set_thumbnail(url=member.avatar_url)
    emb.add_field(name="Registered", value=member.creatd_at.strftime(
        "%A, %B %d, %Y %-H:%M %p %Z"))
    emb.add_field(name="Joined at", value=member.joined_at.strftime(
        "%A, %B %d, %Y %-H:%M %p %Z"))
    emb.add_field(name="Member ID", value=member.id)
    emb.add_field(name=f"Roles ({len(roles)})", value=" ".join(
        [role.mention for role in roles]))
    emb.timestamp = datetime.datetime.now()
    emb.set_footer(text="Powered by Tony",
                   icon_url="https://1.bp.blogspot.com/-WolzwGw_bzU/Xg4MWh4sA7I/AAAAAAAAroA/jwKh4VOv-MIpmz1euxavbP-vshwwCRZQQCLcBGAsYHQ/s1600/101323_original.gif")

    await ctx.send(embed=emb)


@bot.command()
async def imdb(ctx, *, message):
    text = message.split()
    x = "+".join(text)
    url = f"https://api.popcat.xyz/imdb?q={x}"

    async with request("GET", url) as response:
        if response.status == 200:
            data = await response.json()

            btn = nextcord.Button(
                label=f"{data['title']}(IMDb)", style=nextcord.ButtonStyle.link, ulr=data['imdburl'])

            view = View()
            view.add_item(btn)

            emb = nextcord.Embed(
                title=f"{data['title']} ({data['year']})", color=nextcord.Color.random())
            emb.add_field(
                name="Information", value=f"🎬 {data['genres']}\n🎬 Boxoffice: {data['boxoffice']}\n🎬 {data['runtime']}\n🎬 Rated: {data['rating']}/10")
            emb.add_field(name="Actors", value=f"{data['actors']}")
            emb.add_field(name="Dirction", value=f"{data['director']}")
            emb.add_field(name="Screenplay", value=f"{data['writer']}")
            emb.add_field(name="Plot", value=f"{data['plot']}")
            emb.add_field(name="Awards", value=f"{data['awards']}")
            emb.timestamp = datetime.datetime.now()
            emb.set_footer(text="Powered by Tony",
                           icon_url="https://1.bp.blogspot.com/-WolzwGw_bzU/Xg4MWh4sA7I/AAAAAAAAroA/jwKh4VOv-MIpmz1euxavbP-vshwwCRZQQCLcBGAsYHQ/s1600/101323_original.gif")
            emb.set_author(name="IMDb|Internetr Movie Datbase",
                           icon_url="imdb.png")
        else:
            await ctx.send(f"Due to response status {response.status}... there is an error")


@_Q.error
async def Q_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please ask a question❓❓")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command used!!")


@bot.command()
async def whoami(ctx):
    await ctx.send(f"You are {ctx.author.mention}")


@bot.command()
async def inspire(ctx):
    quote = get_quotes()
    await ctx.send(quote)


@bot.command()
async def say_hello_to(ctx, member: nextcord.Member):
    await ctx.send(f"Hello {member.mention}... Wassup😃")


@bot.command()
async def say_bye_to(ctx, member: nextcord.Member):
    await ctx.send(f"Bye {member.mention}... See you again👋")


emails = ["2003", "3524", "377", "420", "069",
          "007", "141", "444", "120", "456", "big_cock"]

passwords = ["Banani2310", "rituja2003", "dadur_bichi", "most_secure_passwd",
             "Uwwwwuuuu", "Vinci2005", "No_one_can_heck_me", "Beluga2.0", "bigben007"]

quotes = ["send me nudes😘", "I'm inevitable", "shake your booty", "FUCK YOU!!",
          "That's pretty nice", "You are so UWU", "Are u sure about that?!"]

randomword = ["Nitro", "Lululululu", "Uwu", "Motherfucker",
              "sexy", "reeeee", "sike", "Ass", "Heck", "LOL", "cg", "fuck"]

ip = ["192.168.29.100", "192.168.29.168",
      "172.19.177.182", "49.37.46.129", "49.56.78.111"]

virus = ["trojan", "big boy", "corona", "phantom"]


@bot.command()
async def heck(ctx, *, member: nextcord.Member):
    message = await ctx.send(f'''Hecking {member.mention} Right Now.. 
  HAHAHAHAHA''')
    await asyncio.sleep(1)

    await message.edit(content=f'''Finding nextcord login...      (2fa 
  bypassed)''')
    await asyncio.sleep(2)

    await message.edit(content=f"""Found:
  Email: `{member.name}{random.choice(emails)}@gmail.com`
  Password: `{random.choice(passwords)}`""")
    await asyncio.sleep(2)

    await message.edit(content=f'''Fetching Dm's with closest friends [if 
  there is any friend]''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Last Dm's 
  {random.choice(quotes)}''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Finding Most common 
  word...''')
    await asyncio.sleep(2)

    await message.edit(content=f''''Most Common = 
  {random.choice(randomword)}''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Injecting the 
  {random.choice(virus)} virus into {member.mention}'s ass''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Virus injected. So much 
  smell🤢🤮''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Setting up a pornhub 
  account for {member.mention}👄..''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Hecking 
  {member.mention}'s' 
  pornhub account...''')
    await asyncio.sleep(2)

    await message.edit(content=f"Finding IP address")
    await asyncio.sleep(2)

    await message.edit(content=f'''IP address: 
  {random.choice(ip)}''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Stealing data from the 
  scary goverment''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Reporting account to 
  nextcord for breaking the TOS...''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Hecking {member.mention}'s 
  google search history😏''')

    await ctx.send(f'''The most Scary and dangerous hacking in 
  the cyber crime history, has been done''')


@bot.command()
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    wallet_amnt = users[str(user.id)]["wallet"]
    bank_amnt = users[str(user.id)]["bank"]

    em = nextcord.Embed(
        title=f"{ctx.author.name}'s balance", color=nextcord.Color.random())
    em.add_field(name="Wallet balance", value=wallet_amnt)
    em.add_field(name="Bank balance", value=bank_amnt)
    await ctx.send(embed=em)


@bot.command()
async def beg(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    earnings = random.randrange(101)

    reply = ["Ah.. You are too much lazy, Go and do some work idiot", f"Oh... You poor begger!! Take {earnings} coins", "Stop it, Get some Help", "You want coins huh?!! But I don't Give a FUCK",
             f"{earnings} coins are deposited to your wallet", "Have a relax.. See You not for mind", "Amar kache paibe shudhu KAACHAA BADAM", f"Okay kid.. Stop crying, {earnings} coins are yours", "Did you ever look yourself in the mirror??"]

    randreply = random.choice(reply)

    await ctx.send(randreply)

    if earnings in randreply:
        users[str(user.id)]["wallet"] += earnings
    else:
        users[str(user.id)]["wallet"] += 0

    with open("users.json", "w") as x:
        json.dump(users, x)


async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("users.json", "w") as x:
        json.dump(users, x)
        return True


async def get_bank_data():
    with open("users.json") as x:
        users = json.load(x)

    return users


@bot.command()
async def prog(ctx):
    emb = nextcord.Embed(
        title="CS JOKES", description=f"{pyjokes.get_joke()}", color=nextcord.Color.random())

    emb.set_author(name="Developer: Ranit Sarkhel",
                   icon_url="https://scontent.fccu2-4.fna.fbcdn.net/v/t1.6435-  9/150911728_416405209458998_2740905449298016969_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=7XgZxKyPF0cAX8beQBu&_nc_ht=scontent.fccu2-4.fna&oh=00_AT-vnEGefmm-5_D8lypwIP4ZQSA1Doc4uwj7AyS-cJMohQ&oe=62FAD3C8")

    emb.set_footer(text="Powered by Tony",
                   icon_url="https://1.bp.blogspot.com/-WolzwGw_bzU/Xg4MWh4sA7I/AAAAAAAAroA/jwKh4VOv-MIpmz1euxavbP-vshwwCRZQQCLcBGAsYHQ/s1600/101323_original.gif")

    emb.timestamp = datetime.datetime.now()
    await ctx.send(embed=emb)


@bot.command()
async def p(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the end of the current song")

    voicechannel = nextcord.utils.get(ctx.guild.channels, name="General")
    await voicechannel.connect()
    voice = nextcord.utils.get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferedcodec': 'mp3', 'preferedquality': '192'}]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(nextcord.FFmpegAudio("song.mp3"))

keep_alive()
bot.run("OTU4MzYzMTM0ODc0MjQzMTI2.YkMPOA.7PdiHwYHM8NBn3D9E1ugbOyNIXw")
