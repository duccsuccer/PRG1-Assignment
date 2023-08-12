# s10257116 Edward Ho - P07/CSF02

import requests
import json


# Use real-time carpark available data from data.gov.sg

def api_data():

    # new list
    api_count = 0
    api_av_list = []
    api_av_dict = {}

    # Get data from data.gov.sg API
    carpark_availability_response = requests.get('https://api.data.gov.sg/v1/transport/carpark-availability')
    response_data = carpark_availability_response.text
    parsed_data = json.loads(response_data)

    # Parse data
    items = parsed_data['items']

    for item in items:

        # 2 items, timestamp and carpark data

        timestamp = item['timestamp']
        carpark_data = item['carpark_data']
        # Print timestamp
        print(f"Timestamp: {timestamp}")

        # Unpack carpark_data
        for cpk_items in carpark_data:

            # 2 items in carpark data, carpark number, carpark info
            cpk_num = cpk_items['carpark_number']

            # Carpark info is a list of dictionaries,
            # loop through to assign values to each variable

            for cpk_info_list in cpk_items['carpark_info']:
                total_lots = cpk_info_list['total_lots']
                lots_ava = cpk_info_list['lots_available']

                # Check if total lots of a carpark is 0 and skip it
                if total_lots == '0':
                    continue

                # Percentage calculation
                lots_percent = int(lots_ava) / int(total_lots) * 100

                # dictionary to store carpark info
                api_av_dict = {"Carpark Number": cpk_num,
                                "Total Lots": total_lots,
                                "Lots Available": lots_ava,
                                "Percentage": lots_percent,
                                }
                # append dictionary to list
                api_av_list.append(api_av_dict)

                # Carpark counter
                api_count += 1
    DONE = True
    return api_av_dict, api_av_list, DONE, api_count

av_dict, av_list, CHECK, counts = api_data()