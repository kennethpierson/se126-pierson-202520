#Ken Pierson
#SE126.04
#Lab #7 - Dictionaries
#2-27-2025

#PROGRAM PROMPT: Build a mini programming dictionary a user can search through and ad to using the words.csv file:
#Access the words.csv file and store the data to a dictionary, where each word in the file is a key of the dictionary and the value stored to each key is the word’s corresponding definition. Then, create a repeatable program that allows a user to interact with the dictionary based on the following menu: 
#My Programming Dictionary Menu
#1.	Show all words – Show all words and their definitions stored to the dictionary
#2.	Search for a word – Allow the user to enter a word and if it is in the dictionary, show its definition (tell the user if the word is not in the dictionary)
#3.	Add a word – Allow a user to add a word and its definition to the dictionary if it does not already exist
#4.	EXIT
#The program should not be case sensitive for user input, and the user should only be able to quit when they have selected menu option number 4.
#Bonus #1 [+5]: When the user is finished using the program, create a new file called updated_words.csv which contains the entire dictionary (including any new words added during the session) and follows the original words.csv field structure (first field is the word, second field is the definition).
#Bonus #2 [+10]: Add a menu option “3.5” which will show all of the words in the dictionary, ordered alphabetically in ascending order (A -> Z)  

#variable dictionary

#--IMPORTS---------------------------------------------
import csv
#--FUNCITONS-------------------------------------------
def loopcontrol(): #() is empty so NO parameters; this function does not require any info to run
  ans = input("\nWould you like to search again? [y/n]: ").lower()
  #check the ans value, repeat back to user if necessary
  while ans != "y" and ans != "n":
    print("***INVALID ENTRY***")
    ans = input("Would you like to search again? [y/n]: ").lower()
  #return the ans value tp be used in the base program!
  return ans

def menu():
    print("\n***My Programming Dictionary Menu***")
    print("1. Show All Words") #Show all words and their definitions stored to the dictionary
    print("2. Search for a Word ") #Allow the user to enter a word and if it is in the dictionary, show its definition (tell the user if the word is not in the dictionary)
    print("3. Add a Word") #Allow a user to add a word and its definition to the dictionary if it does not already exist
    print("4. Exit") #exit the program

    menu_choice = input("Enter your search type [1-4]: ")
    return menu_choice

#we will use the below hand-populated list
valid_menu = ["1", "2", "3", "4"]

#--MAIN EXECUTING CODE---------------------------------
dictionary_entries = {}
with open("text_files\words.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        dictionary_entries.update({rec[0] : rec[1]})

#---DISCONNECT FROM FILE---------------------------------------------------------

answer = "y"
while answer == "y":
    found = [] #reset found list so each new menu/search is is empty
    choice = menu()
    if choice not in valid_menu: 
        print("***INVALID ENTRY***\nPlease try again.\n")
    
    elif choice == "1":
        print(f"\nYou have chosen to Show All Words\n" )
        print(f"{"Word":15} :  {"Definition"}")
        print("-" * 180)
        for key in dictionary_entries:
            #for every key found in the library dictionary
            print(f"{key:15} :  {dictionary_entries[key]}")
        print("-" * 180)
    elif choice == "2":
        print(f"\nYou have chosen to Search for a Word\n" )
        search = input("\nEnter the Word you are looking for: ")
        found = 0
        for key in dictionary_entries:
            if search.lower() == key.lower():
                found = key

        if found != 0:
            print(f"We found your search for {search}, here is the info:\n ")
            print(f"{"Word":15} :  {"Definition"}")
            print("-" * 180)
            print(f"{found:4} : {dictionary_entries[found]}")
            print("-" * 180)
        else:
            print(f"We could not find your search for {search}")
    elif choice == "3":
            print(f"\nYou have chosen to Add a Word\n")
            new_word = input("Please enter the new word: ")
            new_def = input(f"Please enter the definition for {new_word}: ")
            dictionary_entries.update({new_word.lower() : new_def.lower()} )
            for key in dictionary_entries:
                print(f"{key:15} :  {dictionary_entries[key]}")
    elif choice == "4": 
            print("\n---EXIT---")
            answer = "n"
    else:
        print("\t!INVALID ENTRY!")
        #build a way out of the loop - answer should be able to change value!
        if choice == "1" or choice == "2" or choice == "3":
            answer = loopcontrol()
print("\nThank You for using the Program! Good Bye!\n")

#create and write updated_words.csv 
file = open("text_files/updated_words.csv", "w")
length = len(dictionary_entries)
count = 1

for key in dictionary_entries:
    if count <= length - 1:
        file.write(f"{key},{dictionary_entries[key]}\n")
    else:
        file.write(f"{key},{dictionary_entries[key]}")
    count += 1
file.close()