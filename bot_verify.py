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
            with open("data_handling/verification_requests.json", "r") as vr_file:
                # print("Opened verification_requests.json")
                data = json.load(vr_file)

            with open("data_handling/assigned_roles.json", "r") as file:
                # print("Opened assigned_roles.json")
                assigned_roles = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Error reading the JSON file: {e}")
            data = {}
            assigned_roles = {}

        for username, info in data.items():
            # print(username)
            if (
                info["verified"] and username not in assigned_roles
            ):  # Check if the user has visited the link, and if the role has been assigned
                print(f"Attempting to assign role to {username}")
                if await assign_role(username, "Verified"):
                    assigned_roles[username] = True
                    with open("data_handling/assigned_roles.json", "w") as ar_file:
                        json.dump(assigned_roles, ar_file, indent=4)
            else:
                # print(f"Failed to assign role to {username}")
                pass

        # except Exception as e:
        #     print(f"An error occurred: {e}")

        await asyncio.sleep(
            10
        )  # Check every 60 seconds (currently 10 seconds for testing, later change so server wouldn't crash)


async def assign_role(username, role_name):
    guild = bot.guilds[0]  # Assuming the bot is part of one guild
    member = discord.utils.find(lambda m: m.name == username, guild.members)
    if member:
        print(f"Found member {member.name}")
        role = discord.utils.get(guild.roles, name=role_name)
        if role:
            print(f"Role {role} found")
            try:
                await member.add_roles(role)
                print(f"Successfully assigned {role} role to {member.name}")
                return True
            except Exception as e:
                print(f"Error assigning role: {e}")
                return False
    return False


load_dotenv()  # Load environment variables from .env file
bot.run(os.getenv("DISCORD_TOKEN"))
