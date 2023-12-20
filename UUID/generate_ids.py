import uuid
import json


def generate_uuids_for_users(user_ids):
    user_uuid_map = {}
    for user_id in user_ids:
        discord_id = user_ids[user_id]
        user_uuid = str(uuid.uuid4())
        user_uuid_map[discord_id] = user_uuid
    return user_uuid_map


# Load discord_ids from discord_ids.json
with open("UUID/discord_ids.json") as file:
    discord_ids = json.load(file)


# Convert discord_ids to a dictionary
discord_ids_dict = {str(i): discord_ids[i] for i in range(len(discord_ids))}


uuid_map = generate_uuids_for_users(discord_ids_dict)


# Save uuid_map to a JSON file
def save_uuid_map_to_json(uuid_map):
    with open("UUID/uuids.json", "w") as file:
        json.dump(uuid_map, file, indent=4)


# Load discord_emails from discord_emails.json
try:
    with open("UUID/discord_emails.json") as file:
        discord_emails = json.load(file)
except FileNotFoundError:
    discord_emails = {}


# Append UUIDs to discord_emails
def append_uuids_to_discord_emails(discord_emails, uuid_map):
    for email in discord_emails:
        if email in uuid_map:
            if isinstance(discord_emails[email], str):
                discord_emails[email] = {"discord_id": discord_emails[email], "uuid": uuid_map[email], "email": email}
            else:
                discord_emails[email]["discord_id"] = discord_emails[email].get("discord_id", discord_emails[email])
                discord_emails[email]["uuid"] = uuid_map[email]
                discord_emails[email]["email"] = email

# Save updated discord_emails to a JSON file
def save_discord_emails_to_json(discord_emails):
    with open("UUID/discord_emails.json", "w") as file:
        json.dump(discord_emails, file, indent=4)

# Print the updated discord_emails
# print(discord_emails)

if __name__ == "__main__":
    append_uuids_to_discord_emails(discord_emails, uuid_map)
    save_discord_emails_to_json(discord_emails)
