import requests
import json

#  URL of the dataset
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# Make a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    # Save the data to a JSON file
    with open("cso.json", "w") as json_file:
        json.dump(data, json_file)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
