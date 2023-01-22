
import discord, random, os, json
from aiohttp import request
from discord.ext import commands

class santa(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Santa is ready.')

#register: adding user to json dictionary
    @commands.command()
    async def register(self, ctx):
        santa = str(ctx.author.name)
        with open("F:\A_PROGRAMMING\A_VSC\Python\cherry blossoms\santa.json", "r") as f:
            santas = json.load(f)
            if santa not in santas:
                santas[santa] = 0
        with open("F:\A_PROGRAMMING\A_VSC\Python\cherry blossoms\santa.json", "w") as f:
            if santa not in santas:
                santas[santa] = 0
            f.write(json.dumps(santas, indent=5))
        await ctx.send('You have been registered.')

#draw: choosing name for user
    @commands.command()
    @commands.cooldown(1, 10, type = commands.BucketType.user)
    async def draw(self, ctx):
        santa = ctx.author.name
        with open("F:\A_PROGRAMMING\A_VSC\Python\cherry blossoms\santa.json", "r") as f:
            santas = json.load(f)
        ppl = len(santas) - 1
        draw = list(santas.keys())[random.randint(0,ppl)]
        if draw == santa:
            while draw == santa:
                draw = list(santas.keys())[random.randint(0,ppl)]
        else:
            draw = draw
        await ctx.author.send(f"you are {draw}'s Secret Santa!")
        with open("F:\A_PROGRAMMING\A_VSC\Python\cherry blossoms\santa.json", "w") as f:
            santas[santa] = santas.pop(draw)
            ppl = ppl - 1
            f.write(json.dumps(santas, indent=5))

def setup(client):
    client.add_cog(santa(client))
