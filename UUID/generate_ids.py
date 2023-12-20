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

# print(discord_ids)

# Convert discord_ids to a dictionary
discord_ids_dict = {str(i): discord_ids[i] for i in range(len(discord_ids))}

# print(discord_ids_dict)

uuid_map = generate_uuids_for_users(discord_ids_dict)

# Save uuid_map to a JSON file
with open("UUID/uuids.json", "w") as file:
    json.dump(uuid_map, file, indent=4)

# Print the generated UUIDs
# print(uuid_map)
