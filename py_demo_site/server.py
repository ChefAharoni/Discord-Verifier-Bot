from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/verify_user", methods=["GET"])
def verify_user():
    # Extract the UUID from the query parameter
    uuid = request.args.get("uuid")

    # Load the existing data
    try:
        with open("data_handling/verification_requests.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return "Verification data not found", 404

    # Find the user with the matching UUID and update the 'visited' status
    user_found = False
    for user_id, user_info in data.items():
        if user_info["uuid"] == uuid:
            data[user_id]["verified"] = True
            user_found = True
            break

    if not user_found:
        return "User not found", 404

    # Save the updated data
    with open("data_handling/verification_requests.json", "w") as file:
        json.dump(data, file, indent=4)

    return "Verification successful!"


if __name__ == "__main__":
    app.run(port=5000)
