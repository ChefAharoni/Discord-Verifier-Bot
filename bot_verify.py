import discord
import json
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv


intents = discord.Intents.default()
intents.members = True  # Enable intents for member information
intents.messages = True  # Enable intents for message content
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")
    bot.loop.create_task(check_verification_requests())


async def check_verification_requests():
    while True:
        try:
            with open("data_handling/verification_requests.json", "r") as file:
                data = json.load(file)

            for username, info in data.items():
                # print(f"Checking {username}")
                # print(info["verified"])
                if info["verified"]:  # Check if the user has visited the link
                    print(f"Attempting to assign role to {username}")
                    await assign_verified_role(username)
                else:
                    # print(f"Failed to assign role to {username}")
                    pass

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading the JSON file: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

        await asyncio.sleep(
            10
        )  # Check every 60 seconds (currently 10 seconds for testing, later change so server wouldn't crash)


async def assign_verified_role(username):
    guild = bot.guilds[0]  # Assuming the bot is part of one guild
    member = discord.utils.find(lambda m: m.name == username, guild.members)
    print("test line 1")
    if member:
        print("test line 2")
        print(member)
        role = discord.utils.get(guild.roles, name="Verified")
        if role:
            # await member.add_roles(role)
            # print(f"Assigned 'verified' role to {member.name}")
            print("Role found")
            try:
                await member.add_roles(role)
                print(f"Assigned 'verified' role to {member.name}")
                return True
            except Exception as e:
                print(f"Error assigning role: {e}")
                return False
    return False


load_dotenv()  # Load environment variables from .env file
bot.run(os.getenv("DISCORD_TOKEN"))
