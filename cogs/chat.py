import discord
import re
from discord.ext import commands

class chat(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def on_message(self, message):
        if message.author == self.client.user:
            return
        text = message.content
        text = re.sub(r'[^\w\s]','', text).lower().split()
        if "no" in text:
            return
        elif "weeaboo" in text or "weeb" in text:
            await message.channel.send("Nobody here is a weeb or a weeaboo.")
        elif "hello" in text or "hey" in text:
            await message.channel.send("Hello {0.author.name}".format(message) + "-senpai")
        elif "ohayo" in text or "ohayōgozaimasu" in text or "ohayō" in text:
            await message.channel.send("Ohayo {0.author.name}".format(message) + "-senpai")
        elif "ecchi" in text or "hentai" in text:
            await message.channel.send("Are u a pervert? :persevere: {0.author.name}".format(message) + "-senpai")
        elif "nani" in text:
            await message.channel.send("Nani the fuck!?!?")
        elif "oh" in text and "my" in text:
            await message.channel.send("god")

def setup(client):
    client.add_cog(chat(client))
