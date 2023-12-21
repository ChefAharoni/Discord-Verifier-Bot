import gspread
import json

service_account_key_file_path = "UUI/cunyhackathon-uuid-677b2673982f.json"  # File path of the JSON keys access to the Google console

gc = gspread.service_account(
    filename="UUID/cunyhackathon-uuid-677b2673982f.json"
)  # Access the path and open the account

sh = gc.open(
    "HackCUNY: Initial RSVP (Responses)"
)  # Open the shared Google spreadsheet; this sheet was shared with the associated account.


def get_discord_ids():
    """
    Get the Discord IDs from the Google Sheets.

    Returns:
        list: A list of Discord IDs.
    """
    worksheet = sh.sheet1  # Define the worksheet
    discord_ids = [
        value for value in worksheet.col_values(3)[1:] if value
    ]  # Get non-empty values of the third column
    return discord_ids


def get_emails(discord_ids):
    """
    Retrieves the emails associated with the given Discord IDs.

    Args:
        discord_ids (list): A list of Discord IDs.

    Returns:
        dict: A dictionary mapping Discord IDs to their associated emails.
    """
    worksheet = sh.sheet1  # Define the worksheet
    emails = [
        value for value in worksheet.col_values(5)[1:] if value
    ]  # Get non-empty values of the fifth column
    discord_emails = dict(zip(discord_ids, emails))
    return discord_emails


# Save discord_ids to a JSON file
def save_discord_ids_to_json(discord_ids):
    """
    Save the given discord IDs to a JSON file.

    Args:
        discord_ids (list): A list of discord IDs to be saved.

    Returns:
        None
    """
    with open("UUID/discord_ids.json", "w") as file:
        json.dump(discord_ids, file, indent=4)


def save_emails_to_json(discord_emails):
    with open("UUID/discord_emails.json", "w") as file:
        json.dump(discord_emails, file, indent=4)


def get_google_spreads_data():
    discord_ids = get_discord_ids()
    save_discord_ids_to_json(discord_ids)
    discord_emails = get_emails(discord_ids)
    save_emails_to_json(discord_emails)


if __name__ == "__main__":
    get_google_spreads_data()
