import uuid
import json


def generate_uuids_for_users(discord_ids):
    """
    Generate UUIDs for a list of Discord IDs.

    Parameters:
    discord_ids (list): A list of Discord IDs.

    Returns:
    dict: A dictionary mapping each Discord ID to a generated UUID.
    """
    return {discord_id: str(uuid.uuid4()) for discord_id in discord_ids}


def combine_data(discord_ids, discord_emails):
    """
    Combines Discord IDs with corresponding UUIDs and emails.

    Args:
        discord_ids (list): List of Discord IDs.
        discord_emails (dict): Dictionary mapping Discord IDs to emails.

    Returns:
        dict: Dictionary mapping Discord IDs to a dictionary containing UUID and email.
    """
    combined_data = {}
    for discord_id in discord_ids:
        uuid = user_uuid_map[discord_id]
        email = discord_emails.get(discord_id)
        combined_data[discord_id] = {"uuid": uuid, "email": email}
    return combined_data


# Load discord_ids from discord_ids.json
def get_discord_ids():
    """
    Retrieves Discord IDs from a JSON file and generates UUIDs for each ID.

    Returns:
        user_uuid_map (dict): A dictionary mapping Discord IDs to generated UUIDs.
    """
    with open("UUID/discord_ids.json") as di_file:
        discord_ids = json.load(di_file)  # Assuming this is a list of IDs
    user_uuid_map = generate_uuids_for_users(
        discord_ids
    )  # Generate UUIDs for each Discord ID
    return user_uuid_map


# Load discord_emails from discord_emails.json
def get_discord_emails():
    """
    Retrieves the Discord emails from the 'discord_emails.json' file.

    Returns:
        dict: A dictionary mapping ID to email.
    """
    with open("UUID/discord_emails.json") as de_file:
        discord_emails = json.load(
            de_file
        )  # Assuming this is a dict mapping ID to email
    return discord_emails


# Combine data
def combine_ids_and_emails():
    """
    Main function of the module.
    Combines Discord IDs and emails into a dictionary and saves the combined data to a JSON file.

    Returns:
        None
    """
    discord_ids = get_discord_ids()
    discord_emails = get_discord_emails()
    combined_data = combine_data(discord_ids, discord_emails)
    # Save combined data to a JSON file
    with open("UUID/users_data.json", "w") as file:
        json.dump(combined_data, file, indent=4)


def print_combined_data():
    with open("UUID/users_data.json") as file:
        combined_data = json.load(file)
    print(combined_data)


if __name__ == "__main__":
    combine_ids_and_emails()
