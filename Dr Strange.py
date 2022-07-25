from turtle import st
import nextcord
from nextcord.ext import commands
from nextcord.ui import Button, View
import random
import os
import aiohttp
from webserver import keep_alive

bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    print("Things just gone out of hands")


@bot.command()
async def avenger(ctx):
    embed = nextcord.Embed(
        title="AvengerRate", description=f'''You are {random.randrange(101)}% avenger {ctx.author.name}''', color=nextcord.Color.random())

    await ctx.send(embed=embed)


@bot.command()
async def gay(ctx, member: nextcord.Member):
    embed = nextcord.Embed(
        title="GayRate", description=f'''{member.name} is {random.randrange(101)}% gay''', color=nextcord.Color.random())

    await ctx.send(embed=embed)


@bot.command()
async def chutiya(ctx, member: nextcord.Member):
    embed = nextcord.Embed(
        title="ChutiyaRate", description=f'''{member.name} is {random.randrange(101)}% chutiya''', color=nextcord.Color.random())

    await ctx.send(embed=embed)


@bot.command()
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/memes.json") as x:
            memes = await x.json()
            embed = nextcord.Embed(
                color=nextcord.Color.random()
            )
            embed.set_image(url=memes["data"]["children"]
                            [random.randint(0, 25)]["data"]["url"])
            embed.set_footer(
                text=f"Powered by r/memes | Meme requested by {ctx.author.name}")
            await ctx.send(embed=embed)


punch_gifs = ["https://c.tenor.com/axn0K8wofMsAAAAd/thor-punch.gif", "https://c.tenor.com/xbdjwsCznAAAAAAd/hulk-mark-ruffalo.gif", "https://c.tenor.com/4NP-QAjEproAAAAC/avengers-go-to-sleep.gif", "https://c.tenor.com/gBMGs2LMq30AAAAC/thanos-avengers.gif", "https://c.tenor.com/W5h_X5-HiD0AAAAC/thanos-hulk.gif", "https://c.tenor.com/-dK24mwTyKwAAAAC/tv-shows-supernatural.gif", "https://c.tenor.com/2MFfiD2b8iUAAAAC/thanos-punch.gif",
              "https://c.tenor.com/BmS_Z3jvQBwAAAAd/punch-hulk.gif", "https://c.tenor.com/vzMDELlDaN4AAAAC/bh187-justice-league.gif", "https://c.tenor.com/wLCUvXGf974AAAAC/roman-reigns-kevin-owens.gif", "https://c.tenor.com/YOxaBGAHshUAAAAC/justice-league-superman.gif", "https://c.tenor.com/VW4dTQUfWLwAAAAd/peacemaker-white-dragon.gif", "https://c.tenor.com/kw4ICU0Z_RYAAAAC/batfleck-batman.gif"]

punch_LOL = ["https://c.tenor.com/AIudMtNjua0AAAAC/hulk-thor.gif",
             "https://c.tenor.com/DiAEdgV10PgAAAAC/superman-punch.gif", "https://c.tenor.com/rPAg0E9Lh8kAAAAC/punch-fail.gif"]


@bot.command()
async def punch(ctx, member: nextcord.Member):

    punch_command = [f"*{ctx.author.name}* lands a heavyweight punch on *{member.name}*", f"This badass punch shows how much strong *{ctx.author.name}* is", f"By punching *{member.name}*.. *{ctx.author.name}* gets an eternal satisfaction",
                     f"BOOM!! Here comes *{ctx.author.name}*'s punch on *{member.name}*", f"*{ctx.author.name}*'s punch was so delicious that *{member.name}* can't taste it anymore"]

    punch_lol = [f"You're so stupid *{ctx.author.name}*", "How does it feels to being an idiot??",
                 "So you're trying to punch me right??", f"Are your hands ok *{ctx.author.name}*??"]

    if(str(member.name) == "Dr. Strange"):
        embed = nextcord.Embed(color=nextcord.Color.random(
        ), description=random.choice(punch_lol))
        embed.set_image(url=random.choice(punch_LOL))
        embed.set_footer(text="GIF by Dr. Strange",
                         icon_url="https://tenor.com/view/doctor-strange-ready-lets-do-this-gif-25043482.gif")
    else:
        embed = nextcord.Embed(color=nextcord.Color.random(
        ), description=random.choice(punch_command))

        embed.set_image(url=random.choice(punch_gifs))
        embed.set_footer(text="GIF by Dr. Strange",
                         icon_url="https://tenor.com/view/doctor-strange-ready-lets-do-this-gif-25043482.gif")

    await ctx.send(embed=embed)


kick_gifs = ["https://c.tenor.com/3-QcKWquq_IAAAAC/bruce-lee.gif", "https://c.tenor.com/D1q3Z4R5WnkAAAAC/bvnvcbn.gif", "https://c.tenor.com/kWTO0UPS4qEAAAAC/bruce-lee-kick.gif", "https://c.tenor.com/p-n1ssH4UbUAAAAC/captain-america-spiderman.gif", "https://c.tenor.com/t_NY8Buhm2QAAAAC/gtfo-wintersoldier.gif", "https://c.tenor.com/X_0YaTsYQvsAAAAd/thor-thanos.gif", "https://c.tenor.com/Lyqfq7_vJnsAAAAC/kick-funny.gif",
             "https://c.tenor.com/4zwRLrLMGm8AAAAC/chifuyu-chifuyu-kick.gif", "https://c.tenor.com/Qbt44it3rasAAAAC/taiga-aisaka-starling-bg-waifu.gif", "https://c.tenor.com/trxlVJGFkXIAAAAC/sheamus-brogue-kick.gif", "https://c.tenor.com/icV2ba3gU7MAAAAC/kick-anime.gif", "https://c.tenor.com/9PPzm9JjGpsAAAAC/mochi-peach.gif", "https://c.tenor.com/kaqEOE3vZGEAAAAC/hindi-bollywood.gif", "https://c.tenor.com/2EMcdP0soBAAAAAd/cat-gif.gif"]

kick_LOL = ["https://c.tenor.com/lrriroV14NEAAAAd/superman-versus-batman-kick.gif",
            "https://c.tenor.com/hT14hDEqjdgAAAAC/kick-fail.gif"]


@bot.command()
async def kick(ctx, member: nextcord.Member):

    kick_command = [f"And here comes *{ctx.author.name}*'s badass kick. *{member.name}* are u okay??",
                    f"*{ctx.author.name}*'s kick is too strong for *{member.name}*", f"Angry *{ctx.author.name}* lands a superstrong kick on *{member.name}*", f"I think *{member.name}* is no more after dealing such a ruthless kick from *{ctx.author.name}*", f"A really cute kick from {ctx.author.name}"]

    kick_lol = [f"So sorry for that {ctx.author.name}", "YOU TRIED🤣😂",
                f"Outstanding kick {ctx.author.name}. Keep it up"]

    if(str(member.name) == "Dr. Strange"):
        embed = nextcord.Embed(color=nextcord.Color.random(
        ), description=random.choice(kick_lol))
        embed.set_image(url=random.choice(kick_LOL))
        embed.set_footer(text="GIF by Dr. Strange",
                         icon_url="https://tenor.com/view/doctor-strange-ready-lets-do-this-gif-25043482.gif")
    else:
        embed = nextcord.Embed(color=nextcord.Color.random(
        ), description=random.choice(kick_command))

        embed.set_image(url=random.choice(kick_gifs))
        embed.set_footer(text="GIF by Dr. Strange",
                         icon_url="https://tenor.com/view/doctor-strange-ready-lets-do-this-gif-25043482.gif")

    await ctx.send(embed=embed)

ultron = ["https://c.tenor.com/wYflTQ_qESQAAAAC/avengers-ultron.gif", "https://c.tenor.com/r-JrNrQICV0AAAAC/ultron-marvel.gif",
          "https://c.tenor.com/X1QN2-Ako5kAAAAC/angry-ultron.gif", "https://thumbs.gfycat.com/BitesizedRecentCockroach-size_restricted.gif", "https://i.gifer.com/7SXT.gif"]

thanos = ["https://c.tenor.com/y0ZPi77-TZQAAAAd/thanos-smile.gif", "https://data.whicdn.com/images/302340730/original.gif", "https://c.tenor.com/rbcxgOfzFQsAAAAC/thanos-infinity.gif",
          "https://c.tenor.com/qUdBKJFbXzEAAAAC/thanos-avengers-infinity-war.gif", "https://i.pinimg.com/originals/f6/0c/d0/f60cd052dc6b586a43c35c848cd8ef4b.gif"]

dormammu = ["https://c.tenor.com/k743ZSTlniwAAAAd/dormammu-doctor-strange.gif", "https://c.tenor.com/hJ9zXiFhLG8AAAAC/you-dare-doctor-strange.gif", "https://thumbs.gfycat.com/ConcreteSmartBluejay-size_restricted.gif",
            "https://i.pinimg.com/originals/56/2e/67/562e678c95bcd0e513f6ede95c16a635.gif", "https://64.media.tumblr.com/42fb837f87d6b536028849a60662ed01/tumblr_oo45roAgLv1uerxcio5_500.gif"]


class MyButton(Button):
    def __init__(self):
        super().__init__()

    async def callback(self, interaction):
        pass


@bot.command()
async def fight(ctx):
    ultb = Button(label="ULTRON", style=nextcord.ButtonStyle.green)
    thanb = Button(label="THANOS", style=nextcord.ButtonStyle.green)
    dorb = Button(label="DORMAMMU", style=nextcord.ButtonStyle.green)

    v = View()
    v.add_item(ultb)
    v.add_item(thanb)
    v.add_item(dorb)

    await ctx.send("Against whom you want to fight??", view=v)

    rand = random.randrange(40, 61)

    async def button_callback_u(interaction):

        button0 = Button(
            label="Higher", style=nextcord.ButtonStyle.green, emoji="➕")
        buttonB = Button(
            label="BINGO!", style=nextcord.ButtonStyle.green, emoji="🤩")
        button1 = Button(
            label="Lower", style=nextcord.ButtonStyle.green, emoji="➖")

        view = View()
        view.add_item(button0)
        view.add_item(button1)
        Ultron = random.randrange(0, 101)

        emb = nextcord.Embed(title="ULTRON", color=nextcord.Color.random(
        ), description=f"Here comes Ultron and he just chose a secret number between 1 to 100. Is the hidden number is higher or lower than {rand}.\nPress the 'BINGO!' button if you think it's the same number")
        emb.set_image(url=random.choice(ultron))
        emb.set_author(name="Developer: Ranit Sarkhel",
                       icon_url="https://cdn.discordapp.com/attachments/960059262686597126/968760722710487070/FB_IMG_16387282953349342.jpg")
        emb.set_footer(text="GIF by Dr. Strange",
                       icon_url="https://tenor.com/view/doctor-strange-ready-lets-do-this-gif-25043482.gif")

        await ctx.send(embed=emb, view=view)

        async def button_callbackh(interaction):
            if Ultron > rand:
                await interaction.response.send_message("You defeated ultron. Congo!!")
            else:
                await interaction.response.send_message("You Died!! LOL🤣")

        async def button_callbackl(interaction):
            if Ultron < rand:
                await interaction.response.send_message("You defeated ultron. Congo!!")
            else:
                await interaction.response.send_message("You Died!! LOL🤣")

        async def button_callbackB(interaction):
            if Ultron == rand:
                await interaction.response.send_message("You defeated ultron. Congo!!")
            else:
                await interaction.response.send_message("You Died!! LOL🤣")

        button0.callback = button_callbackh
        button1.callback = button_callbackl
        buttonB.callback = button_callbackB

    async def button_callback_t(interaction):

        button0 = Button(
            label="Higher", style=nextcord.ButtonStyle.green, emoji="➕")
        buttonB = Button(
            label="BINGO!", style=nextcord.ButtonStyle.green, emoji="🤩")
        button1 = Button(
            label="Lower", style=nextcord.ButtonStyle.green, emoji="➖")

        view = View()
        view.add_item(button0)
        view.add_item(button1)
        Thanos = random.randrange(0, 101)

        emb = nextcord.Embed(title="THANOS", color=nextcord.Color.random(
        ), description=f"Here comes Thanos and he just chose a secret number between 1 to 100. Is the hidden number is higher or lower than {rand}\nPress the BINGO! button if you think it's the same number")
        emb.set_image(url=random.choice(thanos))
        emb.set_author(name="Developer: Ranit Sarkhel",
                       icon_url="https://cdn.discordapp.com/attachments/960059262686597126/968760722710487070/FB_IMG_16387282953349342.jpg")
        emb.set_footer(text="GIF by Dr. Strange",
                       icon_url="https://tenor.com/view/doctor-strange-ready-lets-do-this-gif-25043482.gif")

        await ctx.send(embed=emb, view=view)

        async def button_callbackh(interaction):
            if Thanos > rand:
                await interaction.response.send_message("You defeated thanos. Congo!!")
            else:
                await interaction.response.send_message("You Died!! LOL🤣")

        button0 = Button(
            label="Higher", style=nextcord.ButtonStyle.green, emoji="➕", disabled=True)
        buttonB = Button(
            label="BINGO!", style=nextcord.ButtonStyle.grey, emoji="🤩", disabled=True)
        button1 = Button(
            label="Lower", style=nextcord.ButtonStyle.grey, emoji="➖", disabled=True)

        async def button_callbackl(interaction):
            if Thanos < rand:
                await interaction.response.send_message("You defeated dormammuthanos Congo!!")
            else:
                await interaction.response.send_message("You Died!! LOL🤣")

        button0 = Button(
            label="Higher", style=nextcord.ButtonStyle.grey, emoji="➕", disabled=True)
        buttonB = Button(
            label="BINGO!", style=nextcord.ButtonStyle.grey, emoji="🤩", disabled=True)
        button1 = Button(
            label="Lower", style=nextcord.ButtonStyle.green, emoji="➖", disabled=True)

        async def button_callbackB(interaction):
            if Thanos == rand:
                await interaction.response.send_message("You defeated thanos. Congo!!")
            else:
                await interaction.response.send_message("You Died!! LOL🤣")

        button0 = Button(
            label="Higher", style=nextcord.ButtonStyle.grey, emoji="➕", disabled=True)
        buttonB = Button(
            label="BINGO!", style=nextcord.ButtonStyle.green, emoji="🤩", disabled=True)
        button1 = Button(
            label="Lower", style=nextcord.ButtonStyle.grey, emoji="➖", disabled=True)

        button0.callback = button_callbackh
        button1.callback = button_callbackl
        buttonB.callback = button_callbackB

    async def button_callback_d(interaction):

        button0 = Button(
            label="Higher", style=nextcord.ButtonStyle.green, emoji="➕")
        buttonB = Button(
            label="BINGO!", style=nextcord.ButtonStyle.green, emoji="🤩")
        button1 = Button(
            label="Lower", style=nextcord.ButtonStyle.green, emoji="➖")

        view = View()
        view.add_item(button0)
        view.add_item(button1)
        Dormammu = random.randrange(0, 101)

        emb = nextcord.Embed(title="DORMAMMU", color=nextcord.Color.random(
        ), description=f"Here comes Dormammu and he just chose a secret number between 1 to 100. Is the hidden number is higher or lower than {rand}\nPress the BINGO! button if you think it's the same number")
        emb.set_image(url=random.choice(dormammu))
        emb.set_author(name="Developer: Ranit Sarkhel",
                       icon_url="https://cdn.discordapp.com/attachments/960059262686597126/968760722710487070/FB_IMG_16387282953349342.jpg")
        emb.set_footer(text="GIF by Dr. Strange",
                       icon_url="https://tenor.com/view/doctor-strange-ready-lets-do-this-gif-25043482.gif")

        await ctx.send(embed=emb, view=view)

        async def button_callbackh(interaction):
            if Dormammu > rand:
                await interaction.response.send_message("You defeated dormammu. Congo!!")
            else:
                await interaction.response.send_message("You Died!! LOL🤣")

        async def button_callbackl(interaction):
            if Dormammu < rand:
                await interaction.response.send_message("You defeated dormammu. Congo!!")
            else:
                await interaction.response.send_message("You Died!! LOL🤣")

        async def button_callbackB(interaction):
            if Dormammu == rand:
                await interaction.response.send_message("You defeated dormammu. Congo!!")
            else:
                await interaction.response.send_message("You Died!! LOL🤣")

        button0.callback = button_callbackh
        button1.callback = button_callbackl
        buttonB.callback = button_callbackB

    ultb.callback = button_callback_u
    thanb.callback = button_callback_t
    dorb.callback = button_callback_d


@bot.command()
async def update(ctx):
    embed = nextcord.Embed(
        title="Announcement", description=f"Two new commands '*punch*' & '*kick*' are added in my commands list. To see the use type '$help <command name>'. You can now punch and kick any member. So just go and beat their ass. Furthur updates will be announced in this channel so stay tuned", color=nextcord.Color.brand_green())

    embed.set_footer(text="Powered by Dr. Strange",
                     icon_url="https://tenor.com/view/doctor-strange-ready-lets-do-this-gif-25043482.gif")

    await ctx.send(embed=embed)


keep_alive()
bot.run(os.environ.get("Dr. Strange secret"))
