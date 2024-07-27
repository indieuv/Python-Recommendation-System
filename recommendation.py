import main
import utilities
import os

dataset = {
    # theme : [token, rating]
    'Tech1': ['development', 0],
    'Tech2': ['programming', 0],
    'Tech3': ['cloud enginner', 0],
    'Tech4': ['coding', 0],
    'Tech5': ['web', 0],

    'Eco1': ['Economy', 0],
    'Eco2': ['Business', 0],
    'Eco3': ['Market', 0],
    'Eco4': ['Stocks', 0]
}

def increaseUserfeed():
    name = utilities.getname()
    file = f'{utilities.profilepath}{name}.txt'

    if os.path.exists(file):
        requests = utilities.readfile(file)
        for request in requests:
            for targetTheme, targetRating in main.userfeed.items():
                for theme, data in dataset.items():
                    if data[0].lower() in request.lower():
                        if targetTheme.lower() in theme.lower():
                            # Change the Value of User Feed
                            main.userfeed[targetTheme] += 1

def increaseGlobalRatings(requests):
    for request in requests:
        for theme, data in dataset.items():
            if data[0].lower() in request.lower():
                # increase the values of dataset itmes
                data[1] += 1

def gatherprofiles():
    profiles = os.listdir(utilities.profilepath)
    
    for profile in profiles:
        file = f'{utilities.profilepath}{profile}'
        requests = utilities.readfile(file)
        increaseGlobalRatings(requests)

def getrecommendation():
    highest_rating = -1
    highest_theme = ''

    highest_dataset_rate = -1
    highest_dataset_token = ''

    for theme, rating in main.userfeed.items():
        if rating > highest_rating:
            highest_rating = rating
            highest_theme = theme
            
    print(f"User Interests : {main.userfeed}\n")

    for theme, data in dataset.items():
        if highest_theme.lower() in theme.lower():
            if data[1] > highest_dataset_rate:
                highest_dataset_rate = data[1]
                highest_dataset_token = data[0]
    
    return highest_dataset_token

if __name__ == '__main__':
    
    print(' - - - - - RECOMMENDATION - - - - - ')
    print(' - - - - - - - - - - - - - - - - - -\n')

    print('1. Show Global Trends.')
    print('2. Show Indivisual Recommendation')

    gatherprofiles()

    choice = input("\n:: Enter Your Choice : ")
    if choice == '1':
        print(dataset)
    elif choice == '2':
        increaseUserfeed()
        print(getrecommendation())

    key = input("")
