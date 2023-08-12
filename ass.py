# s01257116 Edward Ho - P07/CSF02

# Read data from 'carpark-information.csv' at the start of program execution

with open('carpark-information.csv', 'r') as file:
    carpk_dict = {}
    total_cpk = 0
    cpk_list = []
    num_carpk = []
    next(file)
    for line in file:
        # make list of carpark information
        carpk_stuff = line.strip('\n').split(',')
        carpk_no, carpk_type, park_sys, carpk_loc = carpk_stuff[0], carpk_stuff[1], carpk_stuff[2], carpk_stuff[3]
        # dictionary (key = carpark number, value = carpark info list)
        carpk_dict = {"Carpark Number": carpk_no,
                    "Carpark Type": carpk_type,
                    "Type of Parking System": park_sys,
                    "Address": carpk_loc}
        cpk_list.append(carpk_dict)
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
    print("[0] Exit")

count2 = 0
l_count = 0
lots = {}
DONE = False
av_dict = {}
av_list = []
address = None
while True:
    disp()
    option = int(input('Enter your option: '))
    if option == 0:
        break
    if option == 1:
        print("Option 1: Display Total Number of Carparks in 'carpark-information.csv'")
        print(total_cpk)
    elif option == 2:
        print("Option 2: Display All Basement Carparks in 'carpark-information.csv'")
        count = 0
        print('{:<15}{:<19}{:<15}'.format('Carpark No','Carpark Type','Address'))
        for carpk_dict in cpk_list:
            if "BASEMENT" in carpk_dict['Carpark Type']:
                print('{:<15}{:<19}{:<15}'.format(carpk_dict["Carpark Number"], carpk_dict["Carpark Type"], carpk_dict["Address"]))
                count += 1
        print(f'Total Number: {count}')
    elif option == 3:
        filename = input("Enter the file name: ")
        with open(filename, 'r') as file2:
            print(file2.readline())
            next(file2)
            for line in file2:
                availability = line.strip('\n').split(',')
                carpk_num, tot_lots, lots_av = availability[0], availability[1], availability[2]
                if tot_lots == '0':
                    next(file2)
                else:
                    lots_perc = int(lots_av) / int(tot_lots) * 100
                av_dict = {"Carpark Number": carpk_num,
                           "Total Lots": tot_lots,
                           "Lots Available": lots_av,
                           "Percentage": lots_perc,
                           }
                av_list.append(av_dict)
                l_count += 1
        DONE = True

    elif option == 4:
        if DONE is True:
            print(l_count)
        else:
            print('Choose option 3 first!'  )

    elif option == 5:
        if DONE is True:
            for key2, val2 in av_dict.items():
                if int(val2["Lots Available"]) == 0:
                    print(f'Carpark Number: {key2}')
                    count2 += 1
            print(count2)
        else:
            print('Choose option 3 first!')

    elif option == 6:
        if DONE is True:
            per_req = float(input("Enter the percentage required: "))
            print('{:<15}{:<15}{:<17}{:<15}'.format('Carpark No', 'Total Lots', 'Lots Available', 'Percentage'))
            for av_dict in av_list:
                if av_dict["Percentage"] >= per_req:
                    print(f'{av_dict["Carpark Number"]:<15}{av_dict["Total Lots"]:<15}{av_dict["Lots Available"]:<17}{av_dict["Percentage"]:<15.1f}')
                    count2 += 1
            print(f'Total Number: {count2}')
        else:
            print('Choose option 3 first!')

    elif option == 7:
        if DONE is True:
            per_req = float(input("Enter the percentage required: "))
            print('{:<15}{:<15}{:<17}{:<15}{:<15}'.format('Carpark No', 'Total Lots', 'Lots Available', 'Percentage', 'Address'))
            for av_dict in av_list:
                for carpk_dict in cpk_list:
                    if av_dict["Carpark Number"] == carpk_dict["Carpark Number"]:
                        address = carpk_dict["Address"]
                if av_dict["Percentage"] >= per_req:
                    print(f'{av_dict["Carpark Number"]:<15}{av_dict["Total Lots"]:<15}{av_dict["Lots Available"]:<17}{av_dict["Percentage"]:<15.1f}{address}')
                    count2 += 1
            print(f'Total Number: {count2}')
        else:
            print('Choose option 3 first!')
            
    elif option == 8:
        if DONE is True:
            count2 = 1
            loc = input("Location ")
            print('{:<15}{:<15}{:<17}{:<15}{:<15}'.format('Carpark No', 'Total Lots', 'Lots Available', 'Percentage', 'Address'))
            for av_dict in av_list:
                for carpk_dict in cpk_list:
                    if av_dict["Carpark Number"] == carpk_dict["Carpark Number"]:
                        address = carpk_dict["Address"]
                if loc.upper() in address:
                    print(f'{av_dict["Carpark Number"]:<15}{av_dict["Total Lots"]:<15}{av_dict["Lots Available"]:<17}{av_dict["Percentage"]:<15.1f}{address}')
                    count2 += 1
            print(f'Total Number: {count2}')
        else:
            print('Choose option 3 first!')
    elif option == 9:
        lots_list = []
        if DONE is True:
            print('{:<15}{:<15}{:<17}{:<15}{:<15}'.format('Carpark No', 'Total Lots', 'Lots Available', 'Percentage', 'Address'))
            for av_dict in av_list:
                lots_list.append(int(av_dict["Total Lots"]))
            max_lots = max(lots_list)
            
            for av_dict in av_list:
                if str(max_lots) == av_dict["Total Lots"]:
                    address = ""
                    for carpk_dict in cpk_list:
                        if av_dict["Carpark Number"] == carpk_dict["Carpark Number"]:
                            address = carpk_dict["Address"]
                    print(f'{av_dict["Carpark Number"]:<15}{av_dict["Total Lots"]:<15}{av_dict["Lots Available"]:<17}{av_dict["Percentage"]:<15.1f}{address}')
                        
