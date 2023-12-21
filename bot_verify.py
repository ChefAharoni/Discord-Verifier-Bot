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
    """
    Event handler that is triggered when the bot is connected to Discord.
    """
    print(f"{bot.user.name} has connected to Discord!")
    bot.loop.create_task(check_verification_requests())


async def check_verification_requests():
    """
    Asynchronous function that checks for verification requests and assigns roles to verified users.
    """
    while True:
        try:
            with open("data_handling/verification_requests.json", "r") as vr_file:
                data = json.load(vr_file)

            with open("data_handling/assigned_roles.json", "r") as file:
                assigned_roles = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading the JSON file: {e}")
            data = {}
            assigned_roles = {}

        for username, info in data.items():
            if (
                info["verified"] and username not in assigned_roles
            ):  # Check if the user has visited the link, and if the role has been assigned
                print(f"Attempting to assign role to {username}")
                if await assign_role(username, "Verified"):
                    assigned_roles[username] = True
                    with open("data_handling/assigned_roles.json", "w") as ar_file:
                        json.dump(assigned_roles, ar_file, indent=4)
            else:
                # print(f"Failed to assign role to {username}") # Not printing this since it will print all the unverified users, all the time
                pass

        # except Exception as e:
        #     print(f"An error occurred: {e}")

        await asyncio.sleep(60)  # Check every 60 seconds


async def assign_role(username, role_name):
    """
    Asynchronous function that assigns a role to a member in the guild.

    Parameters:
    - username (str): The username of the member to assign the role to.
    - role_name (str): The name of the role to assign.

    Returns:
    - bool: True if the role was successfully assigned, False otherwise.
    """
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
