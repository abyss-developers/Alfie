import asyncio
import datetime
import pytz
import discord
from discord.ext import commands

class admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['purge'])
    @commands.has_any_role('Moderator', 'Admin')
    async def prune(self, ctx, amount=0):
        log = self.client.get_channel(743972548785602591)
        dtp = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('US/Pacific'))
        if amount <= 0:
            await ctx.send("> `AbyssBOT:` Missing Arguments: Amount (Usage: !prune/!purge <amount>)")
        if amount >= 100:
            await ctx.send("> `AbyssBOT`: Please choose a number lower than 100.")
        else:
            await ctx.channel.purge(limit=amount + 1)
            embed = discord.Embed(
                title = "Prune",
                description = "@{} pruned {} messages in {}.".format(ctx.author, amount, ctx.channel),
                colour = discord.Colour.blue()
            )
            embed.set_footer(text = (dtp.strftime('%B %d, %Y at %I:%M %p')))
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')
            await log.send(embed=embed)
    
    @commands.command()
    @commands.has_any_role('Moderator', 'Admin')
    async def kick(self, ctx, member : discord.Member, *, reason=None): # reads that object as a Member object from import discord
        log = self.client.get_channel(743972548785602591)
        dtp = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('US/Pacific'))
        await member.kick(reason=reason)
        print("{} was kicked for reason: {}".format(member, reason))
        await ctx.send("> `AbyssBOT:` {} was kicked for reason: {}".format(member, reason))
        embed = discord.Embed(
            title = "Kick",
            description = "@{} has kicked {} for {}.".format(ctx.author, member, reason),
            colour = discord.Colour.orange()
        )
        embed.set_footer(text = (dtp.strftime('%B %d, %Y at %I:%M %p')))
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')
        await log.send(embed=embed)

    @commands.command()
    @commands.has_role('Admin')
    async def ban(self, ctx, member : discord.Member, *, reason=None): # reads that object as a Member object from import discord
        log = self.client.get_channel(743972548785602591)
        dtp = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('US/Pacific'))
        await member.ban(reason=reason)
        print("{} was banned for reason: {}".format(member, reason))
        await ctx.send("> `AbyssBOT:` {} was banned for reason: {}".format(member.mention, reason))
        embed = discord.Embed(
            title = "Ban",
            description = "@{} has banned {} for {}.".format(ctx.author, member, reason),
            colour = discord.Colour.red()
        )
        embed.set_footer(text = (dtp.strftime('%B %d, %Y at %I:%M %p')))
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')
        await log.send(embed=embed)

    @commands.command()
    @commands.has_any_role('Moderator', 'Admin')
    async def unban(self, ctx, *, member):
        log = self.client.get_channel(743972548785602591)
        dtp = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('US/Pacific'))
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send("> `AbyssBOT:` {} has been unbanned.".format(user.mention))
                embed = discord.Embed(
                    title = "Unban",
                    description = "@{} has unbanned {}.".format(ctx.author, member),
                    colour = discord.Colour.red()
                )
                embed.set_footer(text = (dtp.strftime('%B %d, %Y at %I:%M %p')))
                embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')
                await log.send(embed=embed)
                return
        await ctx.send("> `AbyssBOT:` Cannot find banned user. (Usage: !unban <username#tag>) (Or once again, just ask Jason.)")

    @commands.command()
    @commands.has_any_role('Moderator', 'Admin')
    async def mute(self, ctx, member : discord.Member, *, time=None): # reads that object as a Member object from import discord
        log = self.client.get_channel(743972548785602591)
        dtp = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('US/Pacific'))
        print("{} was muted for time: {}m".format(member, time))
        role = discord.utils.get(member.guild.roles, name="Muted")
        await member.add_roles(role)
        embed = discord.Embed(
            title = "Muted",
            description = "{} was muted for {}m.".format(member.mention, time),
            colour = discord.Colour.purple()
        )
        embed.set_footer(text='Love from the AbyssDEV Team')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')
        await ctx.send(embed=embed)
        embed = discord.Embed(
            title = "Mute",
            description = "@{} has muted {} for {}m.".format(ctx.author, member, time),
            colour = discord.Colour.purple()
        )
        embed.set_footer(text = (dtp.strftime('%B %d, %Y at %I:%M %p')))
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')
        await log.send(embed=embed)
        time = 60 * int(time)
        await asyncio.sleep(time)
        await member.add_roles(role)
        embed = discord.Embed(
            title = "Muted",
            description = "{} was unmuted!".format(member.mention),
            colour = discord.Colour.purple()
        )
        embed.set_footer(text='Love from the AbyssDEV Team')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')
        role = discord.utils.get(member.guild.roles, name="Muted")
        await ctx.send(embed=embed)
        await member.remove_roles(role)

    @commands.command()
    @commands.has_any_role('Moderator', 'Admin')
    async def unmute(self, ctx, member : discord.Member):
        log = self.client.get_channel(743972548785602591)
        dtp = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('US/Pacific'))
        print("{} was unmuted".format(member))
        role = discord.utils.get(member.guild.roles, name="Muted")
        await member.remove_roles(role)
        embed = discord.Embed(
            title = "Muted",
            description = "{} was unmuted!".format(member.mention),
            colour = discord.Colour.purple()
        )
        embed.set_footer(text='Love from the AbyssDEV Team')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')
        role = discord.utils.get(member.guild.roles, name="Muted")
        await ctx.send(embed=embed)
        embed = discord.Embed(
            title = "Unmute",
            description = "@{} has unmuted {}.".format(ctx.author, member),
            colour = discord.Colour.purple()
        )
        embed.set_footer(text = (dtp.strftime('%B %d, %Y at %I:%M %p')))
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')
        await log.send(embed=embed)
        await member.remove_roles(role)

    @commands.command()
    async def control(self, ctx):
        print("Control session started.")
        while True:
            x = input("BOT: ")
            if x == "quit":
                print("Control session stopped.")
                return
            await ctx.send(x)

    @commands.command()
    @commands.has_any_role('Moderator', 'Admin')
    async def shutdown(self, ctx, *, query=""):
        if query == "cancel":
            return
        if query == "confirm":
            embed = discord.Embed(
                title = "Admin Information",
                description = "Please type in your password.",
                colour = discord.Colour.blue()
            )

            embed.set_footer(text='Coded and designed by Jason!')
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')
            embed.set_author(name="Coded in Python by Jason")

            embed.add_field(name="!shutdown cancel", value="Declines the shutdown request", inline=True)
            embed.add_field(name="!shutdown <password>", value="Shutdowns the bot", inline=True)

            await ctx.send(embed=embed)
        if query == "interiorcrocodilealligator":
            raise SystemExit
        if query == "cancel":
            return
        if query == "":
            embed = discord.Embed(
                title = "Shutdown",
                description = "Are you sure you would to shut down?",
                colour = discord.Colour.blue()
            )

            embed.set_footer(text='Coded and designed by Jason!')
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')
            embed.set_author(name="Coded in Python by Jason")

            embed.add_field(name="!shutdown cancel", value="Declines the shutdown request", inline=True)
            embed.add_field(name="!shutdown confirm", value="Shutdowns the bot", inline=True)

            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(admin(client))

if __name__ == "__main__":
    print("You ran the wrong thing! Rookie mistake. lmao")
