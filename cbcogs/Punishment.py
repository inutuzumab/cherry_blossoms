import discord
from discord.ext import commands

class Punishment(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Punishment functions are ready to use.')

#kick
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def kick(self, ctx, member : discord.Member, reason=None):
            await member.kick(reason=reason)
            await ctx.send(f"{member}🤸\n\n\n                                               later bitchhh\n                                    🦽🏌️‍♂️")

#ban
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def ban(self, ctx, member : discord.Member, reason=None):
            await member.ban(reason=reason)
            await ctx.send("🤸\n\n\n                                               later bitchhh\n                                    🦽🏌️‍♂️")

    @kick.error
    async def nimda_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.CheckFailure):
            await ctx.send(f"no. shut up.")
        if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
            await ctx.send(f"no. shut up.")

def setup(client):
    client.add_cog(Punishment(client))
