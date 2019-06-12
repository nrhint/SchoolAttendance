##Nathan Hinton
#This program should check to make ure that everything is set up for the program to run properly.

#Start:

#Vars for the program:
databaseFile = 'Database.db'

requiredFiles = [databaseFile]

def initProgram():
    for file in requiredFiles:
        try:
            open(file, 'r').close()
        except FileNotFoundError:
            print("FILE NOT FOUND: %s"%file)
