import json


# Load data from users_data.json
def load_users_data():
    with open("UUID/users_data.json", "r") as file:
        users_data = json.load(file)
    return users_data


# Initialize verification_requests dictionary
verification_requests = {}


# Process each user entry
def process_user_entry(users_data):
    for discord_id, user_info in users_data.items():
        verification_requests[discord_id] = {
            "uuid": user_info["uuid"],
            "email": user_info["email"],
            "unique_link": user_info["unique_link"],
            "verified": False,  # Initially set to False, indicating the link hasn't been visited yet
        }


# Save the verification_requests to a JSON file
def save_verification_requests():
    with open("data_handling/verification_requests.json", "w") as file:
        json.dump(verification_requests, file, indent=4)


def generate_verify_requests():
    users_data = load_users_data()
    process_user_entry(users_data)
    save_verification_requests()
    print("verification_requests.json has been created.")


if __name__ == "__main__":
    generate_verify_requests()
