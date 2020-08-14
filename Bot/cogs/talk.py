import discord
from discord.ext import commands
import random
import asyncio

class talk(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def kay(self, ctx, *, status=""):
        if status == "what are you up to":
            kayResponses = [
                "school again i hate school",
                "bruh stfu im playing mc",
                "im trying to draw but i gave up",
                "idk what are you doing",
                "nothing lmao"
            ]
            await ctx.me.edit(nick="buyonegetonefree")
            await ctx.send("{}".format(random.choice(kayResponses)))
            await ctx.me.edit(nick="")
        if status == "hi":
            kayResponses = [
                "hello",
                "HI",
                "hihi"
            ]
            await ctx.me.edit(nick="buyonegetonefree")
            await ctx.send("{}".format(random.choice(kayResponses)))
            await ctx.me.edit(nick="")
        if status == "how are you":
            kayResponses = [
                "im good :)",
                "bad",
                "good, u?",
                "Are you Real?"
            ]
            await ctx.me.edit(nick="buyonegetonefree")
            await ctx.send("{}".format(random.choice(kayResponses)))
            await ctx.me.edit(nick="")
        if status == "":
            await ctx.send("> `AbyssBOT:` Please put one of the three sentences. For more info, ask Jason.")

    @commands.command()
    async def enrica(self, ctx, *, status=""):
        if status == "hi":
            enricaResponses = [ 
                "hello",
                "hi",
                "heyo",
            ]
            await ctx.me.edit(nick="Spacceghost")
            await ctx.send("{}".format(random.choice(enricaResponses)))
            await ctx.me.edit(nick="")
        if status == "what are you up to":
            enricaResponses = [ 
                "being tired",
                "big dummie head because I didn't do homework",
                "trying to draw but failing",
            ]
            await ctx.me.edit(nick="Spacceghost")
            await ctx.send("{}".format(random.choice(enricaResponses)))
            await ctx.me.edit(nick="")
        if status == "how are you":
            enricaResponses = [
                "I'm good, you?",
                "Tired, very depresso ._.",
                "Idk, mixed feelings dude",
            ]
            await ctx.me.edit(nick="Spacceghost")
            await ctx.send("{}".format(random.choice(enricaResponses)))
            await ctx.me.edit(nick="")
        if status == "":
            await ctx.send("> `AbyssBOT:` Please put one of the three sentences. For more info, ask Jason.")


    @commands.command()
    async def jason(self, ctx, *, status=""):
        if status == "what are you up to":
            jasonResponses = [
                "Coding atm",
                "doing homework",
                "lmao bro idfk what im doing",
                "talking to u ;)",
                "probably playing league... HAHA BRO U THINK I PLAY LEAUGE"
            ]
            await ctx.me.edit(nick="jatgm")
            await ctx.send("{}".format(random.choice(jasonResponses)))
            await ctx.me.edit(nick="")
        if status == "hi":
            jasonResponses = [
                "hello",
                "ayo whassup",
                "hey"
            ]
            await ctx.me.edit(nick="jatgm")
            await ctx.send("{}".format(random.choice(jasonResponses)))
            await ctx.me.edit(nick="")
        if status == "how are you":
            jasonResponses = [
                "doing pretty well",
                "mmmm good",
                "bad bad bad",
                "AttributionError: EOF when reading a line (32,4)"
            ]
            await ctx.me.edit(nick="jatgm")
            await ctx.send("{}".format(random.choice(jasonResponses)))
            await ctx.me.edit(nick="")
        if status == "":
            await ctx.send("> `AbyssBOT:` Please put one of the three sentences. For more info, ask Jason.")

    @commands.command()
    async def nate(self, ctx, *, status=""):
        if status == "what are you up to":
            nateResponses = [
                "bumberger",
                "your dad",
                "a warm grapefruit with a hole in it"
            ]
            await ctx.me.edit(nick="kandydead")
            await ctx.send("{}".format(random.choice(nateResponses)))
            await ctx.me.edit(nick="")
        if status == "hi":
            nateResponses = [
                "helo",
                "ok",
                "r"
            ]
            await ctx.me.edit(nick="kandydead")
            await ctx.send("{}".format(random.choice(nateResponses)))
            await ctx.me.edit(nick="")
        if status == "how are you":
            nateResponses = [
                "i dont know",
                "tired",
                "in constant fear"
            ]
            await ctx.me.edit(nick="kandydead")
            await ctx.send("{}".format(random.choice(nateResponses)))
            await ctx.me.edit(nick="")
        if status == "":
            await ctx.send("> `AbyssBOT:` Please put one of the three sentences. For more info, ask Jason.")
    
    @commands.command()
    async def therapy(self, ctx):
        embed = discord.Embed(
            title = "Therapy Session Initiliazed",
            description = "You will now get therapy messages every hour!",
            colour = discord.Colour.blue()
        )

        embed.set_footer(text='Coded and designed by Jason!')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')
        embed.set_author(name="Coded in Python by Jason")

        await ctx.send(embed=embed)

        therapyList = [
            '> `AbyssBOT Therapy:` We always have your back, seriously we are right behind you ready to beat up whatever is making you feel sad, even if it\'s you',
            '> `AbyssBOT Therapy:` Your opinions are valid and everyone acknowledges it',
            '> `AbyssBOT Therapy:` Do not overwork yourself, you deserve breaks and a good time',
            '> `AbyssBOT Therapy:` You are a good friend and we appreciate you',
            '> `AbyssBOT Therapy:` The server gets your pain and understands you, we wish you luck and you are cool']

        while True:
            await asyncio.sleep(3600)
            await ctx.send(random.choice(therapyList))

def setup(client):
    client.add_cog(talk(client))

if __name__ == "__main__":
    print("You ran the wrong thing! Rookie mistake. lmao")