import gspread
import json

service_account_key_file_path = "UUI/cunyhackathon-uuid-677b2673982f.json"  # File path of the JSON keys access to the Google console

gc = gspread.service_account(
    filename="UUID/cunyhackathon-uuid-677b2673982f.json"
)  # Access the path and open the account

sh = gc.open(
    "HackCUNY: Initial RSVP (Responses)"
)  # Open the shared Google spreadsheet; this sheet was shared with the associated account.

worksheet = sh.sheet1  # Define the worksheet
discord_ids = worksheet.col_values(3)[1:]  # Get the values of the third column, excluding the first value (header)

# print(discord_ids)

# Save discord_ids to a JSON file
with open("UUID/discord_ids.json", "w") as file:
    json.dump(discord_ids, file, indent=4)
