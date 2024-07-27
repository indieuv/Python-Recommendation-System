import os
import utilities

def addrequests():
    name = utilities.getname()
    file = f'{utilities.profilepath}{name}.txt'

    if os.path.exists(file):

        # clear the file
        with open(file, 'w') as f:
            pass
        
        for i in range(3):
            request = input(f"-> Enter Request {3 - i} : ")
            utilities.writefile(file,request)
    else:
        print("-> Profile Not Found.")

def showrequests():
    name = utilities.getname()
    file = f'{utilities.profilepath}{name}.txt'

    if os.path.exists(file):
        data = utilities.readfile(file)
        print(data)
    else:
        print("-> Profile Not Found.")

if __name__ == '__main__':
    print(' - - - - - REQUEST MNGR - - - - -')
    print(' - - - - - - - - - - - - - - - - -\n')

    print('1. Add Requests')
    print('2. Show Requests\n')

    while True:
        choice = input("\n:: Enter your choice : ")
        if choice == '1':
            addrequests()
        elif choice == '2':
            showrequests()
        else:
            break
