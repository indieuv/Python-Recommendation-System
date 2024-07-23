import os
import utilities
import sys

# create a csv file
def create_profile():
    name = utilities.get_name()

    # create a csv file
    with open(utilities.profile_path + f"{name}.txt", 'a'): 
        print(f":: {name}'s profile has been created.")

# delete a profile
def delete_profile():
    name = utilities.get_name()

    file = utilities.profile_path + f'{name}.txt' 
    
    #delete the file
    if os.path.exists(file):
        os.remove(file)
        print(f":: {name}'s file has been deleted")

if __name__ == '__main__':
    print("\n - - - - - - - - Registeration Screen - - - - - - - - ")
    print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")

    print('1. Create A Profile')
    print('2. Delete A Profile.\n')

    choice = input(':: Enter Your choice : ')
    if choice == '1':
        create_profile()
    elif choice == '2':
        delete_profile()
    else:
        sys.exit()

    exit = input('')