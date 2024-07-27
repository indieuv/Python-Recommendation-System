import subprocess

def openfile(file):
    subprocess.Popen(['python', file], creationflags=subprocess.CREATE_NEW_CONSOLE)

userfeed = {
    'Tech':0,
    'Eco':0
}

registeration = 'registeration.py'
requestmanager = 'requestmanager.py'
recommendation = 'recommendation.py'

if __name__ == '__main__':
    print(' - - - - - MAIN WINDOW - - - - - ')
    print(" - - - - - - - - - - - - - - - - ")

    
    print('\n1. Create Or Delete Profile')
    print('2. Add Or Show Requests ')
    print('3. Calculate Recommendations. \n')

    while True:
        choice = input(":: Enter your choice : ")
        if choice == '1':
            openfile(registeration)
        elif choice == '2':
            openfile(requestmanager)
        elif choice == '3':
            openfile(recommendation)
        else:
            break
