import os
import utilities

def createfile():
    name = utilities.getname()
    profile = f'{utilities.profilepath}{name}.txt'

    with open(profile, 'a') as f:
        print(f"-> {name}'s profile has been created")

def removefile():
    name = utilities.getname()
    profile = f'{utilities.profilepath}{name}.txt'

    if os.path.exists(profile):
        os.remove(profile)
        print(f"-> {name}'s profile has been deleted")
    else:
        print("-> No Such Profile found.")

if __name__ == '__main__':
    print(' - - - - - REGISTERATION - - - - - ')
    print(' - - - - - - - - - - - - - - - - - \n')

    print('1. Create File')
    print('2. Delete File ')
    
    while True:
        choice = input('\n:: Enter your choice : ')
        if choice == '1':
            createfile()
        elif choice == '2':
            removefile()
        else:
            break
