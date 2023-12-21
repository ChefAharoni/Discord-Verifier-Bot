import json


def load_from_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def generate_unique_links(combined_data, base_url):
    unique_links = {}
    for discord_id, info in combined_data.items():
        unique_id = info["uuid"]
        # unique_link = f"{base_url}/assign_role?uuid={unique_id}"
        unique_link = f"{base_url}/verify_user?uuid={unique_id}"
        unique_links[discord_id] = unique_link
        info["unique_link"] = unique_link  # Add unique link to each discord_id
    return unique_links


# base_url = "https://hackcuny.com"  # The website domain
# base_url = "http://127.0.0.1:5000"  # Mock domain for testing (default Flask domain)


# Save the updated data back to the JSON file
def update_users_data(users_data):
    with open("UUID/users_data.json", "w") as file:
        json.dump(users_data, file, indent=4)


def generate_links(base_url):
    users_data = load_from_json("UUID/users_data.json")  # Load the combined data
    unique_links = generate_unique_links(users_data, base_url)
    update_users_data(users_data)


if __name__ == "__main__":
    input_base_url = input("Enter the base URL: ")
    if input_base_url == "":
        base_url = "http://"
    elif input_base_url.lower().startswith("local"):
        base_url = "http://127.0.0.1:5000"
    elif input_base_url.lower().startswith("hack"):
        base_url = "https://hackcuny.com"
    else:
        base_url = input_base_url
    generate_links(base_url)
