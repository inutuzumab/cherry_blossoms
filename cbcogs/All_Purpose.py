import discord, random, json, sys
from discord.ext import commands

#error
def joel(ctx):
    return ctx.author.id != 251608546473410561
class All_Purpose(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'All purpose functions are ready to use.')

#clear
    @commands.command()
    @commands.check(joel)
    async def clear(self, ctx, *, amount):
        number = int(amount) + 1
        await ctx.channel.purge(limit=number)

#coinflip
    @commands.command()
    @commands.check(joel)
    async def coinflip(self, ctx):
        response = ['yes', 'no']
        await ctx.send(f'{random.choice(response)}')

#diceroll
    @commands.command()
    @commands.check(joel)
    async def diceroll(self, ctx):
        roll = ['1','2','3','4','5','6']
        await ctx.send(f'{random.choice(roll)}')

#tok
    @commands.command()
    async def tok(self, ctx):
        if str(ctx.author.id) == "295382372130619392":
            await ctx.send('10')
        else:
            roll = ['1','2','3','4','5','6','7','8','9','10']
            await ctx.send(f'{random.choice(roll)}')

#exit
    @commands.command()
    async def exit(self, ctx):
        sys.exit()    

#error in center_body

def setup(client):
    client.add_cog(All_Purpose(client))
