import discord
import os
import requests
import json

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

# Async library
# Defining an event
@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    print(message)
    await message.channel.send('Hello!')


client.run(os.environ['DISCORD_TOKEN'])
