import os
import _main_window
import utilities

# assuming that these are already calulated
data_set = {
    # Theme : ['token', rating]

    'Tech0': ['coding',0],
    'Tech1': ['programming',0],
    'Tech2': ['web development',0],
    'Tech3': ['game development',0],
    'Tech4': ['cloud engineer',0],
    
    'Eco1': ['property',0],
    'Eco2': ['Business',0],
    'Eco3': ['markets',0],
    'Eco4': ['stock',0]
}

def increase_user_feed(requests):
    for request in requests:
        for desiredTheme, data in data_set.items():
            if data[0].lower() in request.lower(): # we got the desired theme
                # assuming these values are also calculated
                if 'Tech' in desiredTheme:
                    _main_window.user_feed['Tech'] += 1
                elif 'Eco' in desiredTheme:
                    _main_window.user_feed['Eco'] += 1

def increase_global_ratings(requests):
    for request in requests:
        for theme, data in data_set.items():
            # Increase global rating
            if data[0].lower() in request.lower():# data[0] since the first value i.e token is in an array
                data[1] += 1

def calculate_ratings():
    #calculate ratings for each and every file
    profiles = os.listdir(utilities.profile_path)
    for name in profiles:
        file = f'{utilities.profile_path}{name}'
        # get requests
        requests = utilities.read_file(file)

        increase_global_ratings(requests)
            

def show_recommendation():
    userFeed = _main_window.user_feed
    highest_rating = -1 # setting default value
    highest_theme = '' # storing respective theme
    
    highest_data_set_rating = -1 # similar thing for finding the recommended value
    recommended_value = '' # final value

    # find the max ratings from userFeed
    for _theme, _rating in userFeed.items():
        if _rating > highest_rating:
            highest_rating = _rating
            highest_theme = _theme
    
    # find the max value in highest_theme
    for theme, data in data_set.items():
        if highest_theme.lower() in theme.lower():
            if data[1] > highest_data_set_rating:
                highest_data_set_rating = data[1]
                recommended_value = data[0]
                print(data)

    return recommended_value


if __name__ == '__main__':
    print("\n - - - - - - - - Recommenation Panel - - - - - - - - ")
    print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    print('1. Show Gloabl Trends. ')
    print('2. Show Indivisual Recommendation. \n')

    calculate_ratings()
    
    choice = input(":: Enter your choice : ")

    if choice == '1':
        for theme, data in data_set.items():
            print(theme,data)

    elif choice == '2':
        name = utilities.get_name()
        file = f'{utilities.profile_path}{name}.txt'

        if os.path.exists(file):
            requests = utilities.read_file(file)
            increase_user_feed(requests)
            print('')
            print(_main_window.user_feed)

            print(f'\n:: Recommended Value is : {show_recommendation()} ')
    key = input("")