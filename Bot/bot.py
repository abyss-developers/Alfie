import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import sensitivekeys

client = commands.Bot(command_prefix = '!', case_insensitive=True)
client.remove_command('quit')

statuses = cycle([
    'It will get better! I promise you!',
    'If this problem won\'t effect you for the next 5 years, stop thinking about it for the next 5 minutes.',
    'You got this!',
    'Happy Pride Month!',
    'You should treat yourself to a break! Maybe, should I suggest, some youtube?',
    "Get ready for the release of Project: Vencia!",
    "Bored? You should play Project: Zerithin or Duck Runner!",
    'Made with Love by Jason (and feedback from Enrica, Saga, Isabelle, and Acren) <3'])

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(next(statuses)))

@client.event
async def on_ready():
    print("AbyssBOT is now online.")
    print("Coded by Jason, run on Python with Discord.py.")
    print("Please steal with permission!")
    change_status.start()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('> `AbyssBOT:` Please pass in all required arguments (or objects).')
    if isinstance(error, commands.CommandNotFound):
        print("{}: Invalid command used (or mistaken)".format(ctx.message.author))

@client.command(aliases=['bot-commands', 'commands'])
async def _botcommands(ctx):
    embed = discord.Embed(
        title = "Help",
        description = "These are the commands in the AbyssBOT bot! Make sure to ask Jason for any additional help.",
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='Coded and designed by Jason!')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')
    embed.set_author(name="Coded in Python by Jason")

    embed.add_field(name="!kay", value="Talk to Kay virtually!", inline=True)
    embed.add_field(name="!jason", value="Talk to Jason virtually!", inline=True)
    embed.add_field(name="!nate", value="Talk to Nate virtually!", inline=True)
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
