from UUID import get_g_spreads, generate_ids
from data_handling import link_generator, generate_verify_requests

base_url = "https://hackcuny.com"  # The website domain for the unique links


def main():
    """
    This is the main function that executes the data for the Discord Verifier Bot.
    It calls various other functions to perform different tasks such as getting Google Spreadsheets data,
    combining IDs and emails, generating links, and generating verify requests.
    The outcome are two main JSON files: users_data.json and verification_requests.json.
    """
    get_g_spreads.get_google_spreads_data()
    generate_ids.combine_ids_and_emails()
    link_generator.generate_links(base_url)
    generate_verify_requests.generate_verify_requests()
    print("Data has been generated.")


if __name__ == "__main__":
    main()
