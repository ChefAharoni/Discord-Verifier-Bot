import json
import os
import random
import discord
import requests
from replit import db

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

sad_words = [
    "sad", "depressed", "unhappy", "angry", "miserable", "depressing",
    "saddness"
]

starter_encouragements = [
    "Cheer up!", "Hang in there.", "You are a great person"
]

if "responding" not in db:
  db["responding"] = True


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)


def update_encouragements(encouraging_message):
  if "encouragements" in db:
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]


def delete_encouragements(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements


# Async library
# Defining an event
@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$hello'):
    print(message)
    await message.channel.send('Hello!')

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db:
      options = options + list(db["encouragements"])

    if any(word in message.content for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith('$new'):
    encouragement = msg.split("$new ", 1)[1]
    update_encouragements(encouragement)
    await message.channel.send("New encouraging message added.")

  if msg.startswith('$del'):
    encouragements = []
    if "encouragements" in db:
      # index = int(msg.split("$del", 1)[1])
      try:
        index = int(msg.split("$del", 1)[1].strip())
        delete_encouragements(index)
        encouragements = db["encouragements"]
        await message.channel.send(encouragements)
      except ValueError:
        await message.channel.send("Invalid index for deletion.")

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db:
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$responding"):
    value = msg.split("$responding ", 1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")


async def assign_role_to_member(member_id, role_id):
  guild = discord.utils.get(client.guilds, name="HackCUNY 24’")
  if guild:
    member = guild.get_member(member_id)
    if member:
      role = guild.get_role(role_id)
      if role:
        await member.add_roles(role)
        return True
  return False


client.run(os.environ['DISCORD_TOKEN'])
