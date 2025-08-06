import os

from hunterio.client import HunterAPIClient

API_KEY = os.getenv("API_KEY", "bb7566edd1d970b4d11364e993e6e20b1499c79b")

hunter_client = HunterAPIClient(api_key=API_KEY)

# data = hunter_client.search_domain("360solutions.dev")


# data = hunter_client.email_finder("360solutions.dev", first_name="rizwan", last_name="hameed")
# print(data)

# data = hunter_client.verify_email("rizwan.hameed@360solutions.dev")
# print(data)