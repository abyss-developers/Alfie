import discord
from discord.ext import commands
import random
import asyncio

class misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    # events
    @commands.Cog.listener()
    async def on_member_join(self, member : discord.Member):
        print("{} has joined the server.".format(member))
        introduction_channel = self.client.get_channel(715985032099004521)
        embed = discord.Embed(
            title = "{} has joined the server!".format(member),
            description = "Welcome to the server, {}! Please go and look over the rules at #rules. After you get verified, please head on over to #welcome-and-information to read on about the server, or #role-select to select your roles.".format(member),
            colour = discord.Colour.blue()
        )
        embed.set_footer(text='Love from the AbyssDEV Team')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')
        await introduction_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print("{} has left the server.".format(member))
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 754909864584806511:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if payload.emoji.name == '🔴':
                role = discord.utils.get(guild.roles, name='Red')
            if payload.emoji.name == '🩸':
                role = discord.utils.get(guild.roles, name='Scarlet')
            if payload.emoji.name == '🟠':
                role = discord.utils.get(guild.roles, name='Orange')
            if payload.emoji.name == '🟡':
                role = discord.utils.get(guild.roles, name='Yellow')
            if payload.emoji.name == '💴':
                role = discord.utils.get(guild.roles, name='Light yellow')
            if payload.emoji.name == '🥬':
                role = discord.utils.get(guild.roles, name='Electric green')
            if payload.emoji.name == '🟢':
                role = discord.utils.get(guild.roles, name='Green')
            if payload.emoji.name == '👥':
                role = discord.utils.get(guild.roles, name='Teal')
            if payload.emoji.name == '🍏':
                role = discord.utils.get(guild.roles, name='Mint green')
            if payload.emoji.name == '🟦':
                role = discord.utils.get(guild.roles, name='Light blue')
            if payload.emoji.name == '🇦🇨':
                role = discord.utils.get(guild.roles, name='Navy')
            if payload.emoji.name == '🍶':
                role = discord.utils.get(guild.roles, name='Blue')
            if payload.emoji.name == '🟣':
                role = discord.utils.get(guild.roles, name='Light purple')
            if payload.emoji.name == '🍇':
                role = discord.utils.get(guild.roles, name='Purple')
            if payload.emoji.name == '🐖':
                role = discord.utils.get(guild.roles, name='Pink')
            if payload.emoji.name == '💄':
                role = discord.utils.get(guild.roles, name='Hot pink')
            await member.add_roles(role)
        if message_id == 754911450274857002:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if payload.emoji.name == '⚪':
                role = discord.utils.get(guild.roles, name='they/them/theirs')
            if payload.emoji.name == '🔵':
                role = discord.utils.get(guild.roles, name='he/him/his')
            if payload.emoji.name == '🔴':
                role = discord.utils.get(guild.roles, name='she/her/hers')
            if payload.emoji.name == '☄️':
                role = discord.utils.get(guild.roles, name='any pronouns')
            await member.add_roles(role)
        if message_id == 754917774182055978:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if payload.emoji.name == '📣':
                role = discord.utils.get(guild.roles, name='Updates')
            if payload.emoji.name == '📅':
                role = discord.utils.get(guild.roles, name='Events')
            await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == 754909864584806511:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if payload.emoji.name == '🔴':
                role = discord.utils.get(guild.roles, name='Red')
            if payload.emoji.name == '🩸':
                role = discord.utils.get(guild.roles, name='Scarlet')
            if payload.emoji.name == '🟠':
                role = discord.utils.get(guild.roles, name='Orange')
            if payload.emoji.name == '🟡':
                role = discord.utils.get(guild.roles, name='Yellow')
            if payload.emoji.name == '💴':
                role = discord.utils.get(guild.roles, name='Light yellow')
            if payload.emoji.name == '🥬':
                role = discord.utils.get(guild.roles, name='Electric green')
            if payload.emoji.name == '🟢':
                role = discord.utils.get(guild.roles, name='Green')
            if payload.emoji.name == '👥':
                role = discord.utils.get(guild.roles, name='Teal')
            if payload.emoji.name == '🍏':
                role = discord.utils.get(guild.roles, name='Mint green')
            if payload.emoji.name == '🟦':
                role = discord.utils.get(guild.roles, name='Light blue')
            if payload.emoji.name == '🇦🇨':
                role = discord.utils.get(guild.roles, name='Navy')
            if payload.emoji.name == '🍶':
                role = discord.utils.get(guild.roles, name='Blue')
            if payload.emoji.name == '🟣':
                role = discord.utils.get(guild.roles, name='Light purple')
            if payload.emoji.name == '🍇':
                role = discord.utils.get(guild.roles, name='Purple')
            if payload.emoji.name == '🐖':
                role = discord.utils.get(guild.roles, name='Pink')
            if payload.emoji.name == '💄':
                role = discord.utils.get(guild.roles, name='Hot pink')
            await member.remove_roles(role)
        if message_id == 754911450274857002:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if payload.emoji.name == '⚪':
                role = discord.utils.get(guild.roles, name='they/them/theirs')
            if payload.emoji.name == '🔵':
                role = discord.utils.get(guild.roles, name='he/him/his')
            if payload.emoji.name == '🔴':
                role = discord.utils.get(guild.roles, name='she/her/hers')
            if payload.emoji.name == '☄️':
                role = discord.utils.get(guild.roles, name='any pronouns')
            await member.remove_roles(role)
        if message_id == 754917774182055978:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if payload.emoji.name == '📣':
                role = discord.utils.get(guild.roles, name='Updates')
            if payload.emoji.name == '📅':
                role = discord.utils.get(guild.roles, name='Events')
            await member.remove_roles(role)

    # commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('> `AbyssBOT:` Pong! {}ms'.format(round(self.client.latency * 1000)))
    
    @commands.command(aliases=['8ball', 'eightball'])
    async def _8ball(self, ctx, *, question):  # The star means that you can take in like sentences with spaces
        responses = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes - definitely.',
            'You may rely on it.',
            'No lmao bruh',
            'YES! Yes it will be true!',
            'As certain as Luverin\'s upload schedule.',
            'As certain as Nate\'s upload schedule.',
            'As certain as Kay uploading to the #art channel.',
            'As certain as Jason uploading to the #art channel.',
            'As certain as Jason uploading to the #coding channel.',
            'As certain as anyone uploading to the #the-actual-roleplay channel.',
            'No, but i love u too bb <33 0///0',
            'Hmm... I highly doubt it... more likely for Saga to play trumpet then that to happen.',
            'Yes, it will happen, but dude, are your standards so low? That\'s sad even for MY standards.',
            'Heck yes. Like the probability of this message to even be here is one in a fricking million (i tweaked the code)',
            'As certian as anyone looking in the #updates channel lmao',
            'As certian as being a millionare at working at McDonalds',
            'As certian as the things that I am doing are legal',
            'As certian as Riot Games servers being up',
            'As certian as Discord servers being up',
            'As certian as Apple charging good prices for their products',
            'pretty darn certian.'
        ]
        embed = discord.Embed(
            title = "Competitive 8ball",
            description = "Shaking the ball... swish swish",
            colour = discord.Colour.blue()
        )
        embed.set_footer(text='Love from the AbyssDEV Team')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')

        embed.add_field(name=f"{question}", value=f"{random.choice(responses)}")
        
        await ctx.send(embed=embed)

    @commands.command()
    async def annoying(self, ctx):
        await ctx.send("> `AbyssBOT:` You, {}, are {}% annoying.".format(ctx.message.author, round(random.uniform(0,100))))

def setup(client):
    client.add_cog(misc(client))

if __name__ == "__main__":
    print("You ran the wrong thing! Rookie mistake. lmao")
