import json
import os
import discord
import requests

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return quote


# Async library
# Defining an event
@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith("$inspire"):
        quote = get_quote()
        await message.channel.send(quote)


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


client.run(os.environ["DISCORD_TOKEN"])