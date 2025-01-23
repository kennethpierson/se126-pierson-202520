#W7D1 - Intro to Functions

#----IMPORT----
#import only systems from os
from os import system, name
#----FUNCTIONS----
#define our clear function
def clear():

    #for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is posix)
    else:
        _ = system("clear")

#----MAIN CODE----
print("Welcome to my W7D1 program!\n")

input("Press enter to Clear:")
clear()
