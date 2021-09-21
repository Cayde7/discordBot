import discord
import asyncio
import os
import random
import json
from discord.ext import commands

startup_extensions = [
"Cmd.Client",
"Cmd.Waifu",
"Cmd.chat",
"Cmd.Help",
"Cmd.info",
]

client = discord.Client()
client = commands.Bot(command_prefix=("!"),
                      pm_help=True,
                      case_insensitive=True,
                      owner_id=272014773162344449)

client.load_extension("jishaku")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

async def background_loop():
    while True:
        await client.wait_until_ready()
        online = []
        x = client.get_all_members()
        for member in x:
            if member.status == discord.Status.online:
                online.append(member)
            elif member.status == discord.Status.idle:
                online.append(member)
            elif member.status == discord.Status.dnd:
                online.append(member)
        watching = "anime"

        await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=watching, type=3))
        await asyncio.sleep(600)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['It is certain',
                 'Reply hazy, try again',
                 'It is decidedly so',
                 'Ask again later',
                 'Without a doubt',
                 'Better not tell you now',
                 'Yes – definitely',
                 'Cannot predict now',
                 'You may rely on it',
                 'Concentrate and ask again',
                 'As I see it, yes',
                 "Don't count on it",
                 'Most likely',
                 'My reply is no',
                 'Outlook good',
                 'My sources say no',
                 'Yes',
                 'Outlook not so good',
                 'Signs point to yes',
                 'Very doubtful']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

client.loop.create_task(background_loop())
client.run("ODg4ODQwNTA4Mzc2NTE0NjMx.YUYjOw.vWIhGhZNt3LJKjrdmbHKANLGkDY", bot=True, reconnect=True)