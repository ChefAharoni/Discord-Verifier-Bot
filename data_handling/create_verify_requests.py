import json

# Load data from users_data.json
with open("UUID/users_data.json", "r") as file:
    users_data = json.load(file)

# Initialize verification_requests dictionary
verification_requests = {}

# Process each user entry
for discord_id, user_info in users_data.items():
    verification_requests[discord_id] = {
        "uuid": user_info["uuid"],
        "email": user_info["email"],
        "unique_link": user_info["unique_link"],
        "verified": False,  # Initially set to False, indicating the link hasn't been visited yet
    }

# Save the verification_requests to a JSON file
with open("data_handling/verification_requests.json", "w") as file:
    json.dump(verification_requests, file, indent=4)

print("verification_requests.json has been created.")
