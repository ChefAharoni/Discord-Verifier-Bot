import uuid
import json


def generate_uuids_for_users(discord_ids):
    return {discord_id: str(uuid.uuid4()) for discord_id in discord_ids}


def combine_data(discord_ids, discord_emails):
    combined_data = {}
    for discord_id in discord_ids:
        uuid = user_uuid_map[discord_id]
        email = discord_emails.get(discord_id)
        combined_data[discord_id] = {"uuid": uuid, "email": email}
    return combined_data


# Load discord_ids from discord_ids.json
with open("UUID/discord_ids.json") as file:
    discord_ids = json.load(file)  # Assuming this is a list of IDs

# Generate UUIDs for each Discord ID
user_uuid_map = generate_uuids_for_users(discord_ids)

# Load discord_emails from discord_emails.json
with open("UUID/discord_emails.json") as file:
    discord_emails = json.load(file)  # Assuming this is a dict mapping ID to email

# Combine data
combined_data = combine_data(discord_ids, discord_emails)

# Save combined data to a JSON file
with open("UUID/users_data.json", "w") as file:
    json.dump(combined_data, file, indent=4)

# Print to verify
# print(combined_data)
