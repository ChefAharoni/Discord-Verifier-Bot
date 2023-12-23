import json


def load_from_json(file_path):
    """
    Loads data (users data) from a JSON file.
    Opens in a read-only mode.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The loaded data from the JSON file.
    """
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def generate_unique_links(combined_data, base_url):
    """
    Generates unique links for each discord_id in the combined_data dictionary.
    The unique links are generated using the UUIDs.

    Parameters:
    - combined_data (dict): A dictionary containing discord_id as keys and information as values.
    - base_url (str): The base URL used to generate the unique links.

    Returns:
    - unique_links (dict): A dictionary containing discord_id as keys and their corresponding unique links as values.
    """
    unique_links = {}
    for discord_id, info in combined_data.items():
        unique_id = info["uuid"]
        unique_link = f"{base_url}/verify_user?uuid={unique_id}"
        unique_links[discord_id] = unique_link
        info["unique_link"] = unique_link  # Add unique link to each discord_id
    return unique_links


# base_url = "https://hackcuny.com"  # The website domain
# base_url = "http://127.0.0.1:5000"  # Mock domain for testing (default Flask domain)


# Save the updated data back to the JSON file
def update_users_data(users_data):
    """
    Update the users_data dictionary and save it to a JSON file.

    Parameters:
    users_data (dict): The dictionary containing user data.
    """
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
