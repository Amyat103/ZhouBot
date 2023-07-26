import discord
import json
import requests
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")



client.run("MTEzMzU3MDk3MTQzMzk2MzYyMQ.Grn8G3.2AiimsgTMzbLzqJiTjsNdTpAuYEMPs_HR9LfoI")