profile_path = "data/profiles/"

# get the name of the user
def get_name():
    name = input("\n-> Enter your name : ")
    return name

# read a data in a text file
def read_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        data  = file.readlines()
    return data

# write data in a txt file
def write_file(file_path, data):
    with open(file_path, 'a') as file:
        file.write(f"{data}\n")