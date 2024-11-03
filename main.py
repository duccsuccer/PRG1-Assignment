# s10257116 Edward Ho - P07/CSF02


# Import API from data.gov.sg
import requests
import json

# Read data from 'carpark-information.csv' at the start of program execution
with open('carpark-information.csv', 'r') as file:
    carpk_dict = {}
    total_cpk = 0
    cpk_list = []

    # Skip header
    next(file)

    for line in file:

        # Split line into different pieces of information
        carpk_stuff = line.strip('\n').split(',')
        carpk_no, carpk_type, park_sys, carpk_loc = carpk_stuff[0], \
            carpk_stuff[1], carpk_stuff[2], carpk_stuff[3]

        # dictionary to store carpark info
        carpk_dict = {"Carpark Number": carpk_no,
                    "Carpark Type": carpk_type,
                    "Type of Parking System": park_sys,
                    "Address": carpk_loc}

        # append each dictionary into a list
        cpk_list.append(carpk_dict)

        # carpark counter
        total_cpk += 1

# Menu display
def disp():
    print('MENU\n====')
    print("[1] Display Total Number of Carparks in 'carpark-information.csv'")
    print("[2] Display All Basement Carparks in 'carpark-information.csv'")
    print("[3] Read Carpark Availability Data File")
    print("[4] Print Total Number of Carparks in the File Read in [3]")
    print("[5] Display carparks Without Available Lots")
    print("[6] Display Carparks With At Least %x available slots")
    print("[7] Display Addresses of Carparks With At Least %x available slots")
    print("[8] Display All Carparks at Given Location")
    print("[9] Display Carpark with the Most Parking Lots")
    print("[10] Create an Output File with Carpark Availability with Addresses and Sort by Lots Available")
    print("[11] Get real-time carpark availablility data from 'data.gov.sg'")
    print("[0] Exit")

# Option 1
def disp_tot_cpks(total_cpk):
    print("Option 1: Display Total Number of Carparks in 'carpark-information.csv'")
    print(f"Total Number of carparks in 'carpark-information.csv': {total_cpk}.")

# Option 2
def disp_all_basement_cpks(carpk_dict, cpk_list):
    count = 0
    # Table header
    print('{:<15}{:<19}{:<15}'.format('Carpark No','Carpark Type','Address'))
    # Loop through each dictionary
    for carpk_dict in cpk_list:
        # Check for Basement Carparks
        if "BASEMENT" in carpk_dict['Carpark Type']:
            print('{:<15}{:<19}{:<15}'.format(carpk_dict["Carpark Number"], carpk_dict["Carpark Type"], carpk_dict["Address"]))
            count += 1 # Carpark counter
    print(f'Total Number: {count}')

# Option 3
def read_av_file(filename):
    av_dict = {}
    av_list = []
    l_count = 1
    # Open and read availablity file
    with open(filename, 'r') as file2:
            # Print timestamp

            print(file2.readline())
            # Skip Header

            next(file2)

            # Loop through each line in the file
            for line in file2:
                availability = line.strip('\n').split(',')
                carpk_num, tot_lots, lots_av = availability[0], availability[1], availability[2]

                # Skip if total lots
                if tot_lots == '0':
                    next(file2)

                # Percentage calculator
                else:
                    lots_perc = int(lots_av) / int(tot_lots) * 100

                # Dictionary to store availability information
                av_dict = {"Carpark Number": carpk_num,
                            "Total Lots": tot_lots,
                            "Lots Available": lots_av,
                            "Percentage": lots_perc,
                            }

                # Append each dictionary to list
                av_list.append(av_dict)

                # Carpark counter
                l_count += 1
            DONE = True
    return DONE, l_count, av_dict, av_list

# Option 4
def tot_cpks(counts):
    print(f"Total number of carparks in the file: {counts}")

# Option 5
def not_av_cpks(av_dict, av_list, count2):
    for av_dict in av_list:
        if int(av_dict["Lots Available"]) == 0: # Check for full parking lots
            print(f'Carpark Number: {av_dict["Carpark Number"]}')
            count2 += 1 # carpark counter
    print(f"Total number: {count2}")

# Option 6
def x_percent(av_dict, av_list, count2):
    # Percentage requirement from user
    per_req = float(input("Enter the percentage required: "))
    # Header
    print('{:<15}{:<15}{:<17}{:<15}'.format('Carpark No', 'Total Lots', 'Lots Available', 'Percentage'))

    # Loop through dictionaries in the list
    for av_dict in av_list:
        if av_dict["Percentage"] >= per_req: # Check if percentage is greater or equal to requirement
            print(f'{av_dict["Carpark Number"]:<15}{av_dict["Total Lots"]:<15}{av_dict["Lots Available"]:<17}{av_dict["Percentage"]:<15.1f}')
            count2 += 1 # carpark counter
    print(f'Total Number: {count2}')

# Option 7
def x_percent_address(av_dict, av_list, count2, carpk_dict, cpk_list, address):
    # Percentage requirement from user
    per_req = float(input("Enter the percentage required: "))
    # Header
    print('{:<15}{:<15}{:<17}{:<15}{:<15}'.format('Carpark No', 'Total Lots', 'Lots Available', 'Percentage', 'Address'))

    # Loop through dictionaries in the list
    for av_dict in av_list:
        for carpk_dict in cpk_list:
            if av_dict["Carpark Number"] == carpk_dict["Carpark Number"]:
                address = carpk_dict["Address"] # Get the address from the carpark dictionary
        if av_dict["Percentage"] >= per_req: # Check if percentage is greater or equal to requirement
            print(f'{av_dict["Carpark Number"]:<15}{av_dict["Total Lots"]:<15}{av_dict["Lots Available"]:<17}{av_dict["Percentage"]:<15.1f}{address}') # print with address
            count2 += 1 # carpark counter
    print(f'Total Number: {count2}')

# Option 8
def by_address(av_dict, av_list, count2, carpk_dict, cpk_list, address):
    count2 = 1 # reset counter
    loc = input("Location: ") # Location input for user

    # Header
    print('{:<15}{:<15}{:<17}{:<15}{:<15}'.format('Carpark No', 'Total Lots', 'Lots Available', 'Percentage', 'Address'))

    # Loop through dictionaries in the list
    for av_dict in av_list:
        for carpk_dict in cpk_list:
            if av_dict["Carpark Number"] == carpk_dict["Carpark Number"]:
                address = carpk_dict["Address"] # Get the address from the carpark dictionary
        if loc.upper() in address: # Check if the location input is in the address (case-insensitive)
            print(f'{av_dict["Carpark Number"]:<15}{av_dict["Total Lots"]:<15}{av_dict["Lots Available"]:<17}{av_dict["Percentage"]:<15.1f}{address}')
            count2 += 1 # carpark counter
    print(f'Total Number: {count2}')

# Option 9
def max_lots(av_dict, av_list, carpk_dict, cpk_list, address):
    lots_list = []

    # Put all total lots into a list
    for av_dict in av_list:
        lots_list.append(int(av_dict["Total Lots"]))

    # Highest total lots in the list
    max_lots = max(lots_list)

    # Find the carpark matching the total lots
    for av_dict in av_list:
        if str(max_lots) == av_dict["Total Lots"]:
            address = ""
            for carpk_dict in cpk_list:
                if av_dict["Carpark Number"] == carpk_dict["Carpark Number"]:
                    address = carpk_dict["Address"]
                    cpk_type = carpk_dict["Carpark Type"]
                    type_pk = carpk_dict["Type of Parking System"]

            # Print carpark details
            print(f'Carpark Number: {av_dict["Carpark Number"]}')
            print(f'Carpark Type: {cpk_type}')
            print(f'Type of Parking System: {type_pk}')
            print(f'Total Lots: {av_dict["Total Lots"]}')
            print(f'Lots Available: {av_dict["Lots Available"]}')
            print(f'Percentage: {av_dict["Percentage"]:.1f}%')
            print(f'Address: {address}')

# Option 10
def write_file(av_dict, av_list, carpk_dict, cpk_list, address):
    # Make and open new file
    newfile = open("carpark-availability-with-addresses.csv", 'x')
    newfile.write('Carpark No,Total Lots,Lots Available,Address\n')

    sorted_av_list = sorted(av_list, key = get_lots_available)
    # Loop through each dictionary in the list
    for av_dict in sorted_av_list:
        for carpk_dict in cpk_list:
            if av_dict["Carpark Number"] == carpk_dict["Carpark Number"]:
                address = carpk_dict["Address"]
        newfile.write(f'{av_dict["Carpark Number"]},{av_dict["Total Lots"]},{av_dict["Lots Available"]},{address}\n')
    newfile.close()

# Option 11
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

# lots available key
def get_lots_available(av_dict):
    return int(av_dict["Lots Available"])

# Main Program

address = None
count2 = 0
CHECK = False
while True:
    disp()
    # Validation
    try:
        option = int(input('Enter your option: '))
        if option < 0 or option > 11:
            print("Enter a number from 0-10!")
    except ValueError:
        print("Please enter a number!")

    # Options
    if option == 0:
        break
    if option == 1:
        disp_tot_cpks(total_cpk)
    elif option == 2:
        print("Option 2: Display All Basement Carparks in 'carpark-information.csv'")
        disp_all_basement_cpks(carpk_dict, cpk_list)
    elif option == 3:
        print("Option 3: Read Carpark Availability Data File")
        filename = input("Enter the file name: ")
        CHECK, counts, av_dict, av_list = read_av_file(filename)
    elif option == 4:
        # Validation to see if option 3 or 11 is already selected
        if not CHECK:
            print("Select Option 3 First!")
        else:
            print("Option 4: Print Total Number of Carparks in the File Read in [3]")
            tot_cpks(counts)
    elif option == 5:
        if not CHECK:
            print("Select Option 3 First!")
        else:
            print("Option 5: Display carparks Without Available Lots")
            not_av_cpks(av_dict, av_list, count2)
    elif option == 6:
        if not CHECK:
            print("Select Option 3 First!")
        else:
            print("Option 6: Display Carparks With At Least %x available slots")
            x_percent(av_dict, av_list, count2)
    elif option == 7:
        if not CHECK:
            print("Select Option 3 First!")
        else:
            print("Option 7: Display Addresses of Carparks With At Least %x available slots")
            x_percent_address(av_dict, av_list, count2, carpk_dict, cpk_list, address)
    elif option == 8:
        if not CHECK:
            print("Select Option 3 First!")
        else:
            print("Option 8: Display All Carparks at Given Location")
            by_address(av_dict, av_list, count2, carpk_dict, cpk_list, address)
    elif option == 9:
        if not CHECK:
            print("Select Option 3 First!")
        else:
            print("Option 9: Display Carpark with the Most Parking Lots")
            max_lots(av_dict, av_list, carpk_dict, cpk_list, address)
    elif option == 10:
        if not CHECK:
            print("Select Option 3 First!")
        else:
            print("Option 10: Create an Output File with Carpark Availability with Addresses and Sort by Lots Available")
            write_file(av_dict, av_list, carpk_dict, cpk_list, address)
    elif option == 11:
        print("Option 11: Get real-time carpark availablility data from 'data.gov.sg'")
        av_dict, av_list, CHECK, counts = api_data()
