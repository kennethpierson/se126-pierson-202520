#Ken Pierson
#SE126.04
#W1D2 Lab Demo: SE116 Review
#1-13-2025 [W1D2]

#PROGRAM PROMPT: It is a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program. 

#VARIABLE DICTIONARY
#anwser             loop control; value determines if loop repeats, entered by the user
#meeting_name       input for the meeting name
#people             input for the number of people attanding the meeting
#max_cap            input for the maximum capacity of the meeting room
#allow              calcuation for capacity - attendees
#conv               converters if a negative to a positive

#--------IMPORTS----------------------------------------------

from os import system, name

#--------FUNCTIONS--------------------------------------------

def clear():
    if name == "nt": #for windows
        _ = system("cls")
    else: #for mac or linux
        _ = system("clear")

def decision(): #<--FUNCTION HEADER
    #this function asks a user if they'd like to enter another temp. checks the response for validity, and then returns a valid response back to the main program
    ans = input("Would you like to enter another meeting? [y/n]: ").lower()
    #user error trap loop - ensures user provides valid value
    while ans != "y" and ans != "n":
        print("***INVAILD ENTRY!***")
        ans = input("Would you like to enter another meeting? [y/n]: ").lower()
    return ans #this value will replace the function call in the main code

def difference(people, max_cap):
    diff = max_cap - people
    return diff

def get_name():
    name = (input("\nPlease enter the meeting name: "))
    return name

def get_ppl():        
    ppl = int(input("How many people will be attending?: "))
    return ppl

def get_cap_max():
    cap_max = int(input("What is the capacity of the room?:"))
    return cap_max

#--------MAIN EXECUTING CODE----------------------------------

print("\n***Fire Safety Room Capacity Check***\n")

answer = "y" #loop control variable

#start of loop - will be based on answer, and user can change value at end of loop
while answer == "y":
    meeting_name = get_name()
    people = get_ppl()
    max_cap = get_cap_max()

    allow = difference(people, max_cap) #calulates user input 
    if people <= max_cap:
        print(f"\nThe {meeting_name} meeeting can be held as it meets the fire safety code")
        print(f"You can add {allow} more people and still be fire safety compliant! ")
    elif people > max_cap:
        conv = allow * -1 #If a negative number is recieved this converts it to a positive
        print(f"\nThe {meeting_name} meeting CANNOT be held as it is in VIOLATION of fire safety code")
        print(f"You must remove {conv} people to be fire saftey compliant")
    print()
    answer = decision() #return value will replace this function call and store to "response"
    clear()

#out of loop

print("\nThank you for using the program. Goodbye.")