import requests
import json

# Make the API request
carpark_availability_response = requests.get('https://api.data.gov.sg/v1/transport/carpark-availability')
response_data = carpark_availability_response.text
parsed_data = json.loads(response_data)

# Access the list of items
items = parsed_data['items']

# Iterate through the list and access the 'timestamp' for each item
for item in items:
    timestamp = item['timestamp']
    carpark_data = item['carpark_data']
    for dict1 in carpark_data:
        for items2 in dict1['carpark_info']:
            print(type(items2['total_lots']))
