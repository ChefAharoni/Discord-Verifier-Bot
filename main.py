from UUID import get_g_spreads, generate_ids, link_generator

base_url = "https://hackcuny.com"  # The website domain


def main():
    get_g_spreads.get_google_spreads_data()
    generate_ids.combine_ids_and_emails()
    link_generator.generate_links(base_url)


if __name__ == "__main__":
    main()
