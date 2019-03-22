import requests

url = "https://api.skypicker.com/locations?type=subentity&term=GB&locale=en-US&active_only=false&location_types=airport&limit=999&sort=name"

response = requests.get(url)
data = response.json()

print(data)
