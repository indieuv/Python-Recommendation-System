import subprocess
import time

recommendation_file = '_recommendation.py'
registeration_file = 'user_registeration.py'
request_manager = 'manage_requests.py'

# assuming these values are also calculated
user_feed = {
    'Tech':0,
    'Eco':0
}

# open a file
def open_file(file):
    time.sleep(1)

    # open the file
    subprocess.Popen(['python',file], creationflags=subprocess.CREATE_NEW_CONSOLE)


# user interface
def userInterface():
    print("\n - - - - - - - - Registeration Screen - - - - - - - - ")
    print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    print('1. Create or Delete Profile. ')
    print('2. Add or Remove Requests. ')
    print('3. Calculate Recommendations. ')
    print('4. Exit\n')

    while True:
        choice = input(":: Enter your choice : ")

        if choice == '1':
            open_file(registeration_file)
        elif choice == '2':
            open_file(request_manager)
        elif choice == '3':
            open_file(recommendation_file)
        elif choice == '4' or choice == '':
            break
        else:
            print("-> Invalid Choice")

if __name__ == "__main__":
    userInterface()