import random, os, discord, json
from discord.ext import commands, tasks
from itertools import cycle

token = 'this is for csesoc'
client = commands.Bot(command_prefix = 'mmh ', aliases = 'Mmh ')

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.dnd, activity = discord.Game('>>help'))
    print('Cherry blossoms begin to bloom.')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cbcogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cbcogs.{extension}')

@client.command()
async def sayhello(ctx):
    await ctx.send("hello ewen")
    
for filename in os.listdir('F:\A_PROGRAMMING\A_VSC\Python\cherry blossoms\cbcogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cbcogs.{filename[:-3]}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cbcogs.{extension}')
    client.load_extension(f'cbcogs.{extension}')
    await ctx.send(f"{extension} has been reloaded.")

#error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        min = str(error.retry_after / 60)
        sec = error.retry_after % 60
        await ctx.send(f'You are too tired to search for another Pokémon. Try again in {min[0]} minutes and {sec:,.0f} seconds.')
    else:
        raise error

client.run(token)
