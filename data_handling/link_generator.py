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
base_url = "http://127.0.0.1:5000"  # Mock domain for testing

users_data = load_from_json("UUID/users_data.json")  # Load the combined data
unique_links = generate_unique_links(users_data, base_url)


# Save the updated data back to the JSON file
def update_users_data():
    with open("UUID/users_data.json", "w") as file:
        json.dump(users_data, file, indent=4)


if __name__ == "__main__":
    update_users_data()

# for i in unique_links:
#     print(i)
#     print(unique_links[i])
#     print()
# print(unique_links)
