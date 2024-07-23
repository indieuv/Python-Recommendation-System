import utilities
import os
import sys

# add requests to a file
def add_requests():
    name = utilities.get_name()
    file = f'{utilities.profile_path}{name}.txt'


    if os.path.exists(file):
        # get requests
        i = 0
        for i in range(3):
            request = input(f":: Request {3 - i} : ")
            # store requests
            utilities.write_file(file, request)
    else:
        print(":: Profile not found.")   

# show all the request made by the user
def remove_requests():
    name = utilities.get_name()
    file = f'{utilities.profile_path}{name}.txt'

    request_to_remove = input(":: Enter the request you want to remove : ")

    if os.path.exists(file):
        # read the file 
        with open(file, 'r') as f:
            lines = f.readlines()

        with open(file, 'w') as f:
            for line in lines:
                if not request_to_remove in line:
                    f.write(line)
                else:
                    pass

def show_requests():
    name = utilities.get_name()
    file = f'{utilities.profile_path}{name}.txt'

    if os.path.exists(file):
        data = utilities.read_file(file)
        print('')
        for d in data:
            print(d, end="\r")

if __name__ == '__main__':
    print("\n - - - - - - - - Request Manager - - - - - - - - - ")
    print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")

    print('1. Add Requests.')
    print('2. Remove Requests. ')
    print('3. Show Requests.\n')

    while True:
        choice = input(':: Enter your choice : ')
        if choice == '1':
            add_requests()
        elif choice == '2':
            remove_requests()
        elif choice == '3':
            show_requests()
        else:
            break

    exit = input('')