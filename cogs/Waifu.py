import discord
import random
from discord.ext import commands

class vrc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def Waifu(self, ctx):
        await ctx.send(random.choice(ctx.guild.members).name +" is curently the best waifu")

    @commands.command()
    async def Husbando(self, ctx):
        await ctx.send(random.choice(ctx.guild.members).name +" is curently the best husbando")

def setup(client):
    client.add_cog(vrc(client))
