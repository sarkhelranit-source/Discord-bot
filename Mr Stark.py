import nextcord
from nextcord.ext import commands
from nextcord.ui import Button, View
import os
import asyncio
import io
import string
import openai
import oneliners
import random
import datetime
import math
from aiohttp import request
import requests
import json
from webserver import keep_alive

intents = nextcord.Intents.all()
intents.message_content = True
intents.typing = True
intents.members = True
intents.guilds = True

api_key = os.environ.get("api_key")


bot = commands.Bot(command_prefix=".", case_insensitive=True, intents=intents)


@bot.command()
async def prog(ctx, *, message):
  txt = message.split()
  x = " ".join(txt)
  
  prompt = f'''Convert this text to a programmatic command:

  Example:{x}
  Output:'''

  response = openai.Completion.create(api_key=api_key, engine="text-davinci-002",  prompt=prompt, max_tokens=100)
  await ctx.reply(f"```\n{response['choices'][0]['text'][2:]}\n```")
  
  
@bot.command()
async def speak(ctx, *, message):
  txt = message.split()
  x = " ".join(txt)
  
  prompt = f"""You:{x}
  Friend:"""

  response = openai.Completion.create(api_key=api_key, engine="text-davinci-002",  prompt=prompt, max_tokens=60)

  res = response["choices"][0]["text"]

  if res[0] == "\n" and res[1] == "\n":
    await ctx.send(res[2:])
  else:
    await ctx.send(res)


@bot.command()
async def mte(ctx, *, message):
  txt = message.split()
  x = " ".join(txt)
  
  prompt = f"""Convert movie titles into emoji.

  Back to the Future: 👨👴🚗🕒 
  Batman: 🤵🦇 
  Transformers: 🚗🤖
  {x}:"""

  response = openai.Completion.create(api_key=api_key, engine="text-davinci-002", prompt=prompt, max_tokens=60)
  await ctx.send(response["choices"][0]["text"][1:])


@bot.command()
async def wanted(ctx, member: nextcord.Member):
    url = f"https://api.popcat.xyz/wanted?image={member.avatar.url}"

    async with request("GET", url) as response:
        imgdata = io.BytesIO(await response.read())
        welcimg = nextcord.File(imgdata, "imgdata.png")

        if member.name == "RASODA":
            await ctx.send("https://c.tenor.com/HWBMmc8g6p4AAAAM/fuck-fuck-you.gif")
        else:
            await ctx.send(file=welcimg)


@bot.command()
async def distract(ctx, member1: nextcord.Member, member2: nextcord.Member, member3: nextcord.Member):
    url = f"https://vacefron.nl/api/distractedbf?boyfriend={member1.avatar.url}&woman={member2.avatar.url}&girlfriend={member3.avatar.url}"

    async with request("GET", url) as response:
        imgdata = io.BytesIO(await response.read())
        file = nextcord.File(imgdata, "imgdata.png")

        if ctx.author.name != "RASODA" and (member1.name == "RASODA" or member2.name == "RASODA" or member3.name == "RASODA"):
            await ctx.reply("https://c.tenor.com/9ajZkvVxdS8AAAAM/akshay-kumar-rakh-teri-maa-ki-rakh.gif")
        elif ctx.author.name != "RASODA" and (member1.name == "Wanda" or member2.name == "Wanda" or member3.name == "Wanda"):
            await ctx.reply("https://c.tenor.com/kjaYAvyiLCEAAAAM/itni-choti-si-baat-pe-hugg-diye-mirzapur.gif")
        else:
            await ctx.send(file=file)


@bot.command()
async def yell(ctx, member1: nextcord.Member, member2: nextcord.Member):
    url = f"https://vacefron.nl/api/womanyellingatcat?woman={member1.avatar.url}&cat={member2.avatar.url}"
    
    async with request("GET", url) as response:
        imgdata = io.BytesIO(await response.read())
        file = nextcord.File(imgdata, "imgdata.png")
        
        if member1.name == "RASODA" or member1.name == "Wanda" or member1.name == bot.user.name:
            await ctx.reply("https://c.tenor.com/jLbcu4lgIyoAAAAM/bhool-bhulaiyaa-akshay-kumar-aditya.gif")
        else:
            await ctx.send(file=file)


@bot.command()
async def pat(ctx, member: nextcord.Member):
    url = f"https://api.popcat.xyz/pet?image={member.avatar.url}"

    async with request("GET", url) as response:
        imgdata = io.BytesIO(await response.read())
        welcimg = nextcord.File(imgdata, "imgdata.gif")

        if member.name == "RASODA":
            await ctx.send("https://c.tenor.com/-d8ZvWiLXWwAAAAM/abe-hatt-abe-hat.gif")
        else:
            await ctx.reply(file=welcimg)


@bot.command()
async def ship(ctx, member1: nextcord.Member, member2: nextcord.Member):
    url = f"https://api.popcat.xyz/ship?user1={member1.avatar.url}&user2={member2.avatar.url}"

    async with request("GET", url) as response:
        imgdata = io.BytesIO(await response.read())
        welcimg = nextcord.File(imgdata, "imgdata.png")

        if (member1.name == "Wanda" and member2.name == "RASODA") or (member1.name == "RASODA" and member2.name == "Wanda"):
            await ctx.reply(file=welcimg)
        elif member1.name == "RASODA" or member2.name == "RASODA":
            await ctx.send("https://c.tenor.com/2QICKZczOQYAAAAM/3idiots-chatur-ramalingam.gif")
        elif member1.name == "Wanda" or member2.name == "Wanda":
            await ctx.send("https://c.tenor.com/rCwUWeWaDCgAAAAM/lund-lele.gif")
        elif member1.name == bot.user.name or member2.name == bot.user.name:
            await ctx.send("https://c.tenor.com/qYQWj6tJV_kAAAAM/zakir-zakirkhan.gif")
        else:
            await ctx.reply(file=welcimg)


@bot.command()
async def dog(ctx):
    url = "https://some-random-api.ml/facts/dog"

    async with request("GET", url) as response:
        data = await response.json()
        emb = nextcord.Embed(
            title="Dog Facts", description=data['fact'], color=nextcord.Color.random())
        emb.timestamp = datetime.datetime.now()
        emb.set_footer(
            text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        emb.set_author(name="Developer: Ranit Sarkhel",
                       icon_url="https://scontent.fccu2-4.fna.fbcdn.net/v/t1.6435-9/150911728_416405209458998_2740905449298016969_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=7XgZxKyPF0cAX8beQBu&_nc_ht=scontent.fccu2-4.fna&oh=00_AT-vnEGefmm-5_D8lypwIP4ZQSA1Doc4uwj7AyS-cJMohQ&oe=62FAD3C8")
        emb.set_thumbnail(
            url="https://i.pinimg.com/originals/5f/05/2b/5f052b5b7375c79ad256aa65c55fece0.gif")
        await ctx.send(embed=emb)


@bot.command()
async def cat(ctx):
    url = "https://some-random-api.ml/facts/cat"

    async with request("GET", url) as response:
        data = await response.json()
        emb = nextcord.Embed(
            title="Cat Facts", description=data['fact'], color=nextcord.Color.random())
        emb.timestamp = datetime.datetime.now()
        emb.set_footer(
            text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        emb.set_author(name="Developer: Ranit Sarkhel",
                       icon_url="https://scontent.fccu2-4.fna.fbcdn.net/v/t1.6435-9/150911728_416405209458998_2740905449298016969_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=7XgZxKyPF0cAX8beQBu&_nc_ht=scontent.fccu2-4.fna&oh=00_AT-vnEGefmm-5_D8lypwIP4ZQSA1Doc4uwj7AyS-cJMohQ&oe=62FAD3C8")
        emb.set_thumbnail(url="https://c.tenor.com/NFjEeHbk-zwAAAAC/cat.gif")
        await ctx.send(embed=emb)


@bot.command()
async def pwd(ctx, message):
    num = int(message)
    lst = string.printable

    passwd = []
    passwd.extend(list(lst))
    random.shuffle(passwd)

    emb = nextcord.Embed(
        title="Password", description=f"Your {num} character password is:\n `{''.join(passwd[0:(num)])}`", color=ctx.author.color)
    emb.set_footer(
        text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
    emb.timestamp
    emb.timestamp = datetime.datetime.now()
    await ctx.author.send(embed=emb)


@bot.command()
async def trig(ctx, *, member: nextcord.Member):
    url = f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar.url}'

    async with request("GET", url) as response:
        triggf = io.BytesIO(await response.read())
        file = nextcord.File(triggf, "trigger.gif")
        emb = nextcord.Embed(
            title=f"Trigerred {member.name}", color=member.color)
        emb.set_image(url="attachment://trigger.gif")
        emb.set_footer(
            text=f"requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        emb.timestamp = datetime.datetime.now()
        await ctx.reply(embed=emb, file=file)


@bot.command()
async def amgsus(ctx, member: nextcord.Member):
    lst = ["true", "false"]

    url = f"https://some-random-api.ml/premium/amongus?avatar={member.avatar.url}&key=5rQWsDuewFB9s6HvXMU6USvEGthn2rzmBdt28KOB6dnOY9s9DUzDqftgijnGbGgt&username={member.name}&imposter={random.choice(lst)}"

    async with request("GET", url) as response:
        amgs = io.BytesIO(await response.read())
        file = nextcord.File(amgs, "amgs.gif")
        emb = nextcord.Embed(color=member.color)
        emb.set_image(url="attachment://amgs.gif")
        emb.set_author(
            name="Among Sus", icon_url="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/ad09b7110700277.5ff3fbebc5f27.gif")
        emb.set_footer(
            text=f"requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        emb.timestamp = datetime.datetime.now()
        await ctx.reply(embed=emb, file=file)


@bot.command()
async def horny(ctx, *, member: nextcord.Member):
    url = f"https://some-random-api.ml/canvas/horny?avatar={member.avatar.url}"
    if member == None:
        await ctx.send("Please mention someone")
    elif member.name == "RASODA":
        await ctx.send("RASODA is not horny at all")
    else:
        async with request("GET", url) as response:
            hor = io.BytesIO(await response.read())
            file = nextcord.File(hor, "horny.png")
            emb = nextcord.Embed(
                title=f"Horny License just for {member.name}", color=member.color)
            emb.set_image(url="attachment://horny.png")
            emb.set_author(
                name="Horny", icon_url="https://discord.com/channels/943127717157675009/998642909345755326/1002977602614595594")
            emb.set_footer(
                text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
            emb.timestamp = datetime.datetime.now()
            await ctx.reply(embed=emb, file=file)


@bot.command()
async def simp(ctx, *, member: nextcord.Member):
    url = f"https://some-random-api.ml/canvas/simpcard?avatar={member.avatar.url}"
    if member == None:
        await ctx.send("Please mention someone")
    elif member.name == "RASODA":
        await ctx.send("RASODA is not a simp")
    else:
        async with request("GET", url) as response:
            smp = io.BytesIO(await response.read())
            file = nextcord.File(smp, "simp.png")
            emb = nextcord.Embed(
                title=f"Simpcard for {member.name}", color=member.color)
            emb.set_image(url="attachment://simp.png")
            emb.set_footer(
                text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
            await ctx.reply(embed=emb, file=file)


@bot.command()
async def fac(ctx, *, num: int):
    await ctx.send(math.factorial(num))


@bot.command()
async def info(ctx, *, member: nextcord.Member):
    emb = nextcord.Embed(title=member.name, color=member.color)
    emb.add_field(name="Registered", value=member.created_at.strftime(
        "%a, %b %d, %Y %I:%M:%S %p %Z"))
    emb.add_field(name="Joined", value=member.joined_at.strftime(
        "%a, %b %d, %Y %I:%M:%S %p %Z"))
    emb.add_field(name="Roles", value=", ".join(
        role.mention for role in member.roles))
    emb.add_field(
        name="Status", value=f"Mobile: {member.mobile_status}\nDesktop: {member.desktop_status}\nWeb: {member.web_status}")
    emb.add_field(name="Top Role", value=member.top_role.mention)
    emb.set_thumbnail(url=member.avatar.url)
    emb.set_footer(
        text=f"ID: {member.id}", icon_url="https://1.bp.blogspot.com/-WolzwGw_bzU/Xg4MWh4sA7I/AAAAAAAAroA/jwKh4VOv-MIpmz1euxavbP-vshwwCRZQQCLcBGAsYHQ/s1600/101323_original.gif")
    emb.set_author(
        name=f"{member.name}#{member.discriminator}", icon_url=member.avatar.url)
    emb.timestamp = datetime.datetime.now()
    await ctx.send(embed=emb)


@bot.command()
async def inspire(ctx):
    responses = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(responses.text)

    emb = nextcord.Embed(
        title="Quotes", description=f"{json_data[0]['q']}", color=nextcord.Color.random())
    emb.add_field(name="Author", value=f"{json_data[0]['a']}")
    emb.set_author(name="Developer: Ranit Sarkhel",
                   icon_url="https://scontent.fccu2-4.fna.fbcdn.net/v/t1.6435-9/150911728_416405209458998_2740905449298016969_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=7XgZxKyPF0cAX8beQBu&_nc_ht=scontent.fccu2-4.fna&oh=00_AT-vnEGefmm-5_D8lypwIP4ZQSA1Doc4uwj7AyS-cJMohQ&oe=62FAD3C8")
    emb.set_footer(text="Powered by Tony",
                   icon_url="https://1.bp.blogspot.com/-WolzwGw_bzU/Xg4MWh4sA7I/AAAAAAAAroA/jwKh4VOv-MIpmz1euxavbP-vshwwCRZQQCLcBGAsYHQ/s1600/101323_original.gif")

    emb.timestamp = datetime.datetime.now()
    await ctx.send(embed=emb)


@bot.command()
async def pokemon(ctx, *, message):
    text = message.split()
    x = "+".join(text)
    url = f"https://some-random-api.ml/pokedex?pokemon={x}"

    async with request("GET", url) as response:
        data = await response.json()
        emb = nextcord.Embed(
            title=f"{data['name'].title()}", url=f'''https://www.pokemon.com/us/pokedex/{data['name'].title()}''', description=f"{data['description']}", color=nextcord.Color.random())
        emb.add_field(name="Type", value=", ".join(
            type for type in data['type']))
        emb.add_field(name="Abilities", value=", ".join(
            abl for abl in data['abilities']))
        emb.add_field(name="Height and Weight",
                      value=f"Height: {data['height']}\nWeight: {data['weight']}")
        emb.add_field(
            name="Stats", value=f'''🩸HP: {data['stats']['hp']}\n\n🤺Attack: {data['stats']['attack']}\n\n🛡Defense: {data['stats']['defense']}\n\n⚔Special Attack: {data['stats']['sp_atk']}\n\n🗡Special Defense: {data['stats']['sp_def']}\n\n🏃‍♂️Speed: {data['stats']['speed']}\n\n Total: {data['stats']['total']}''')
        emb.set_thumbnail(url=data['sprites']['normal'])
        emb.set_image(url=data['sprites']['animated'])

        emb.set_author(name="Pokemon",
                       icon_url="https://i.gifer.com/Se26.gif")
        emb.set_footer(text="Powered by Tony",
                       icon_url="https://1.bp.blogspot.com/-WolzwGw_bzU/Xg4MWh4sA7I/AAAAAAAAroA/jwKh4VOv-MIpmz1euxavbP-vshwwCRZQQCLcBGAsYHQ/s1600/101323_original.gif")
        emb.timestamp = datetime.datetime.now()
        await ctx.send(embed=emb)


# @bot.command()
# async def wiki(ctx, *, msg:str):
#   text = msg.split()
#   x = "_".join(text)
#   url = f"https://en.wikipedia.org/wiki/{x}"

#   emb = nextcord.Embed(title=msg.title(), description=wikipedia.summary(msg), color=nextcord.Color.random(), url=url)
#   pass


@bot.command()
async def wyr(ctx):
    res = requests.get("https://api.popcat.xyz/wyr")
    data = json.loads(res.text)

    emb = nextcord.Embed(title="WOULD YOU RATHER",
                         color=nextcord.Color.random())

    emb.add_field(name="Option1", value=f"{data['ops1']}")
    emb.add_field(name="Option2", value=f"{data['ops2']}")

    emb.set_author(name="Developer: Ranit Sarkhel",
                   icon_url="https://scontent.fccu2-4.fna.fbcdn.net/v/t1.6435-9/150911728_416405209458998_2740905449298016969_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=7XgZxKyPF0cAX8beQBu&_nc_ht=scontent.fccu2-4.fna&oh=00_AT-vnEGefmm-5_D8lypwIP4ZQSA1Doc4uwj7AyS-cJMohQ&oe=62FAD3C8")

    emb.set_footer(text="Powered by Tony",
                   icon_url="https://1.bp.blogspot.com/-WolzwGw_bzU/Xg4MWh4sA7I/AAAAAAAAroA/jwKh4VOv-MIpmz1euxavbP-vshwwCRZQQCLcBGAsYHQ/s1600/101323_original.gif")

    emb.timestamp = datetime.datetime.now()
    await ctx.send(embed=emb)


@bot.command()
async def lyrics(ctx, *, message):
    text = message.split()
    x = "+".join(text)
    url = f"https://api.popcat.xyz/lyrics?song={x}"

    async with request("GET", url) as response:
        data = await response.json()
        if response.status == 200:
            emb = nextcord.Embed(title=f"{data['title']} by {data['artist']}",
                                 description=f"{data['lyrics']}", color=nextcord.Color.random())
            emb.set_thumbnail(url=data['image'])
            emb.set_author(
                name="Spotify", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Spotify_App_Logo.svg/2048px-Spotify_App_Logo.svg.png")
            emb.set_footer(text="Powered by Tony",
                           icon_url="https://1.bp.blogspot.com/-WolzwGw_bzU/Xg4MWh4sA7I/AAAAAAAAroA/jwKh4VOv-MIpmz1euxavbP-vshwwCRZQQCLcBGAsYHQ/s1600/101323_original.gif")
            emb.timestamp = datetime.datetime.now()
            await ctx.send(embed=emb)
        else:
            await ctx.send(f"Due to response status {response.status}... there is an error")


@bot.command()
async def imdb(ctx, *, message):
    text = message.split()
    x = "+".join(text)
    url = f"https://api.popcat.xyz/imdb?q={x}"

    async with request("GET", url) as response:
        if response.status == 200:
            data = await response.json()
            btn = Button(label=f"{data['title']}(IMDb)",
                         style=nextcord.ButtonStyle.link, url=data['imdburl'])

            view = View()
            view.add_item(btn)

            emb = nextcord.Embed(
                title=f"{data['title']} ({data['year']})", color=nextcord.Color.random())
            emb.add_field(
                name="Information", value=f"🎭 {data['genres']}\n💸 Boxoffice: {data['boxoffice']}\n🎬 {data['runtime']}\n💯 Rated: {data['rating']}/10")
            emb.add_field(name="Actors", value=f"{data['actors']}")
            emb.add_field(name="Direction", value=f"{data['director']}")
            emb.add_field(name="Screenplay", value=f"{data['writer']}")
            emb.add_field(name="Plot", value=f"{data['plot']}")
            emb.add_field(name="Awards", value=f"{data['awards']}")
            emb.set_thumbnail(url=f"{data['poster']}")
            emb.timestamp = datetime.datetime.now()
            emb.set_footer(text="Powered by Tony",
                           icon_url="https://1.bp.blogspot.com/-WolzwGw_bzU/Xg4MWh4sA7I/AAAAAAAAroA/jwKh4VOv-MIpmz1euxavbP-vshwwCRZQQCLcBGAsYHQ/s1600/101323_original.gif")
            emb.set_author(name="IMDb | Internet Movie Database")
            await ctx.send(embed=emb, view=view)
        elif data['type'] == "series" and response.status == 200:
            await ctx.send(embed=emb, view=view)
        else:
            await ctx.send(f"Due to response status {response.status}... there is an error")


@bot.command()
async def joke(ctx):
    r = requests.get("https://some-random-api.ml/joke")
    data = json.loads(r.text)
    emb = nextcord.Embed(
        title="Jokes", description=f"{data['joke']}", color=nextcord.Color.random())
    emb.add_field(name="Author", value=f"{bot.user.name}")
    emb.set_author(name="Developer: Ranit Sarkhel",
                   icon_url="https://scontent.fccu2-4.fna.fbcdn.net/v/t1.6435-9/150911728_416405209458998_2740905449298016969_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=7XgZxKyPF0cAX8beQBu&_nc_ht=scontent.fccu2-4.fna&oh=00_AT-vnEGefmm-5_D8lypwIP4ZQSA1Doc4uwj7AyS-cJMohQ&oe=62FAD3C8")

    emb.set_footer(text="Powered by Tony",
                   icon_url="https://1.bp.blogspot.com/-WolzwGw_bzU/Xg4MWh4sA7I/AAAAAAAAroA/jwKh4VOv-MIpmz1euxavbP-vshwwCRZQQCLcBGAsYHQ/s1600/101323_original.gif")

    emb.timestamp = datetime.datetime.now()
    await ctx.send(embed=emb)


@bot.command()
async def say(ctx):
    emb = nextcord.Embed(
        title="Oneliners", description=f"{oneliners.get_random()}", color=nextcord.Color.random())

    emb.set_author(name="Developer: Ranit Sarkhel",
                   icon_url="https://scontent.fccu2-4.fna.fbcdn.net/v/t1.6435-9/150911728_416405209458998_2740905449298016969_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=7XgZxKyPF0cAX8beQBu&_nc_ht=scontent.fccu2-4.fna&oh=00_AT-vnEGefmm-5_D8lypwIP4ZQSA1Doc4uwj7AyS-cJMohQ&oe=62FAD3C8")

    emb.add_field(name="Author", value=f"{bot.user.name}")

    emb.set_footer(text="Powered by Tony",
                   icon_url="https://1.bp.blogspot.com/-WolzwGw_bzU/Xg4MWh4sA7I/AAAAAAAAroA/jwKh4VOv-MIpmz1euxavbP-vshwwCRZQQCLcBGAsYHQ/s1600/101323_original.gif")

    emb.timestamp = datetime.datetime.now()
    await ctx.send(embed=emb)


@bot.command()
async def agify(ctx, *, member):
    url = f"https://api.agify.io/?name={member}"

    async with request("GET", url) as response:
        data = await response.json()
        await ctx.send(f"{data['name']}'s age is {data['age']}")


@bot.command()
async def gen(ctx, *, member):
    url = f"https://api.genderize.io?name={member}"

    async with request("GET", url) as response:
        data = await response.json()
        await ctx.send(f"{data['name']} is a {data['gender']}. probabilty of being a {data['gender']} {data['probability']*100}%")


@bot.command()
async def ping(ctx):
    await ctx.send(f"Hey there! what's up\nHere is the current latency: {round(bot.latency * 1000)}ms")


@bot.command(name="8ball")
async def ball8(ctx, *, question):
    text = question.split()
    x = "%20".join(text)
    url = f"https://8ball.delegator.com/magic/JSON/{x}"

    async with request("GET", url) as response:
        data = await response.json()
        await ctx.send(data['magic']['answer'])


@bot.command()
async def choose(ctx, *, message):
    txt = message.split()
    if "RASODA" in message:
        await ctx.send(f"I will choose 👉 RASODA")
    else:
        await ctx.send(f"I will choose 👉 {random.choice(txt)}")


@bot.command()
async def clear(ctx, amount: int):
    if ctx.author.name == "RASODA":
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.send("Sorry this command is only for the owner")

    if (amount == 1):
        await ctx.send(f"{amount} message is deleted")
    elif(amount > 1):
        await ctx.send(f"{amount} messages got deleted")
    else:
        await ctx.send("DON'T ACT LIKE A DUMB😑")


@bot.command()
async def ban(ctx, member: commands.MemberConverter):
    await ctx.guild.ban(member)
    await ctx.send(f"{member.mention} is banned for doing chugli in the server")


@bot.command()
async def unban(ctx, *,  member):
    banned_users = await ctx.guild.ban()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please give a specific amount of message you want to clear")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command used!!")


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
    message = await ctx.send(f'''Hecking {member.mention} Right Now... HAHAHAHAHA''')
    await asyncio.sleep(1)

    await message.edit(content=f'''Finding discord login...(2fa bypassed)''')
    await asyncio.sleep(2)

    await message.edit(content=f"""Found Victim's Email: {member.name}{random.choice(emails)}@gmail.com & Password: {random.choice(passwords)}""")
    await asyncio.sleep(2)

    await message.edit(content=f'''Fetching Dm's with closest friends[if there is any friend]''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Last Dm: {random.choice(quotes)}''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Finding the Most common word...''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Most Common word = {random.choice(randomword)}''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Injecting the {random.choice(virus)} virus into {member.mention}'s ass''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Virus injected. So much smell🤢🤮''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Setting up a pornhub account for {member.mention}👄..''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Hecking {member.mention}'s' pornhub account...''')
    await asyncio.sleep(2)

    await message.edit(content=f"Finding IP address")
    await asyncio.sleep(2)

    await message.edit(content=f'''IP address: {random.choice(ip)}''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Stealing data from the scary goverment''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Reporting account to nextcord for breaking the TOS...''')
    await asyncio.sleep(2)

    await message.edit(content=f'''Hecking {member.mention}'s google search history😏''')

    await ctx.send(f'''The most Scary and dangerous heck in 
the cyber crime history, has been done''')


keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
bot.run(TOKEN)
