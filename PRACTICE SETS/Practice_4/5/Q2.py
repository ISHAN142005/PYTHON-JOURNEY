"""
Install and import the requests module (if available) and use it to fetch data from "https://api.github.com".
"""

import requests

url = "https://api.github.com"
response = requests.get(url)

if response.status_code == 200:  # Here we are checking status code . 200 means OK
    print("Successfully fetched data from GitHub!")
    data = response.json()  # -->This is converting JSON data to Python dictionary

    print("Here are some useful details:")
    print("Current user URL:", data.get("current_user_url"))
    print("Authorizations URL:", data.get("authorizations_url"))
    print("Repository search URL:", data.get("repository_search_url"))
else:
    print(
        "Failed to fetch data. Status code:", response.status_code
    )  # IF WE ENTER THIS ELSE THEN OUTPUT WILL BE 404 NOT FOUND OR 500 SERVER ERROR
