import requests
import base64
import json

url = "https://api.merge.dev/api/accounting/payments/"

# set initial query parameters as needed
params = {
    "limit": 10,
    "offset": 0
}

# make initial API call to get the first page of results
response = requests.get(url, params=params)

# parse response to get previous link
previous_link = "cj0xJnA9MjAyMS0wMS0wNiswMyUzQTI0JTNBNTMuNDM0MzI2JTJCMDAlM0EwMA=="

# if a previous link exists, make a new API call to retrieve the previous page of results
if previous_link:
    # decode previous link and extract query parameters
    previous_params = json.loads(base64.b64decode(previous_link.split("?")[1]).decode("utf-8"))

    # make new API call to get the previous page of results
    response = requests.get(url, params=previous_params)

# process results as needed
api_response = response.json()["results"]
pprint(api_response)
