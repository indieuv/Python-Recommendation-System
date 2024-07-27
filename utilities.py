profilepath = 'profiles/'

def getname():
    name = input(":: Enter your name : ")
    return name

# read a file
def readfile(file):
    data = []
    with open(file, 'r') as f:
        data = f.readlines()
    return data

# write file
def writefile(file, request):
    with open(file, 'a') as f:
        f.write(f'{request}\n')
