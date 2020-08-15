import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import sensitivekeys

client = commands.Bot(command_prefix = '!', case_insensitive=True)
client.remove_command('quit')

statuses = cycle([
    'Welcome to the Xephians server!',
    'My prefix is !. Try "!help"',
    'You got this!',
    "Follow @jaqarx on Instagram!",
    "Follow @acren.io on Instagram!",
    "Follow @_sagastine_ on Instagram!"])

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(next(statuses)))

@client.event
async def on_ready():
    print("AbyssBOT is now online.")
    print("Coded by Jason, run on Python with Discord.py.")
    print("Please steal with permission!")
    change_status.start()


@client.command(aliases=['bot-commands', 'commands'])
async def _botcommands(ctx):
    embed = discord.Embed(
        title = "Help",
        description = "These are the commaneds for Alfie.",
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='Made by AbyssDEV!')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')
    embed.set_author(name="AbyssDEV")

    embed.add_field(name="!8ball", value="Play 8ball!", inline=True)
    embed.add_field(name="!ping", value="Shows bot latency (ping)", inline=True)
    embed.add_field(name="!prune", value="Prunes for you (and works!)", inline=True)
    embed.add_field(name="!annoying", value="Insecure? You're in luck!", inline=True)
    embed.add_field(name="!rules <integer>", value="Stay informed on the rules!", inline=True)

    await ctx.send(embed=embed)

@client.command()
async def load(ctx, extention):
    client.load_extension("cogs.{}".format(extention))

@client.command()
async def unload(ctx, extention):
    client.unload_extension("cogs.{}".format(extention))

@client.command()
async def reload(ctx, extention):
    client.unload_extension("cogs.{}".format(extention))
    client.load_extension("cogs.{}".format(extention))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension("cogs.{}".format(filename[:-3])) # cuts example.py to example
    
client.run(sensitivekeys.connect)
