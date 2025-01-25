#Name Ken Pierson
#W9 # Lab 6
#Date December 8, 2024
#SE116.02

#Construct a program that will analyze potential voters. The program should generate the following totals:
#1. Number of individuals not eligible to register.
#2. Number of individuals who are old enough to vote but have not registered.
#3. Number of individuals who are eligible to vote but did not vote.
#4. Number of individuals who did vote.
#5. Number of records processed.
#The program must prompt the user for the ID number, age, if the person is registered to vote, and if the person voted. You will also have to prompt to see if the user has more data to enter.

#VARIABLE DICTIONARY
#total_not_eligible_to_register
#total_old_enough_not_registered
#total_eligible_did_not_vote
#total_voters
#total_records_processed
#answer = input
#id_number
#voter_age
#registered
#voted

#---IMPORTS---------------------------------------------------
from os import system, name
#---FUNCTIONS-------------------------------------------------
def clear():
    if name == "nt": #for windows
        _ = system("cls")
    else: #for mac or linux
        _ = system("clear")

def loopcontrol(): #() is empty so NO parameters; this function does not require any info to run
    ans = input("Would you like to enter more data? [y/n]: ").lower()
    while ans != "y" and ans != "n":
      print("***INVALID ENTRY***")
      ans = input("Would you like to enter more data? [y/n]: ").lower()
    return ans

def get_age_integer():  
  age = input("Enter the Voter's age: ")
  #.isnumeric() used to check if all the characters are numeric: It returns True if all characters in the string are numeric. It returns False if even one character in the string is not numeric.
  if age.isnumeric() and int(age) > 0:
    return int(age) 
  else:
    print("***INVALID ENTRY***") 
    return get_age_integer()

def get_id_integer(): 
  id = input("Enter the Voter ID Number: ")
  if id.isnumeric() and int(id) >= 0: 
    return int(id) 
  else:
    print("***INVALID ENTRY***") 
    return get_id_integer()


def registration():
  reg = input("Is the individual Registered to Vote [y/n]: ").lower()
  while reg != "y" and reg != "n":
    print("***INVALID ENTRY***")
    reg = input("Is the individual Registered to Vote [y/n]: ").lower()
  return reg

def actually_voted():
  vote = input("Did the individual Vote [y/n]: ").lower()
  while vote != "y" and vote != "n":
    print("***INVALID ENTRY***")
    vote = input("Did the individual Vote [y/n]: ").lower()
  return vote   

#---------------------------------------------------------------------

#start code below :]

clear()
print("Welcome to Voter Analysis Tool!\n")

total_not_eligible_to_register = 0
total_old_enough_not_registered = 0
total_eligible_did_not_vote = 0
total_voters = 0
total_records_processed = 0

answer = input("Would you like to start the Voter Analysis Tool? [y/n]: ").lower()

#invalid entry trap - user will only enter this if they do not follow the directions from prior prompt
while answer != "y" and answer != "n":
  print("***INVALID ENTRY***")
  answer = input("Would you like to start the Voter Analysis Tool? [y/n]: ").lower()

#"When checking to see if the user wants to enter more data they should be able to enter a y or a Y.(lowercase()"
#main program loop - repeats for each voter
while answer == "y":

  id_number = get_id_integer()
  voter_age = get_age_integer()
  registered = registration()
  voted = actually_voted()

  #update running counts and totals for end of program
 
  if voter_age < 18:
    total_not_eligible_to_register += 1
  if voter_age >= 18 and registered == "n":
    total_old_enough_not_registered += 1
  if voter_age >= 18 and registered == "y" and voted == "n":
    total_eligible_did_not_vote += 1
  if voted == "y":
    total_voters += 1

  total_records_processed = total_records_processed + 1

  print(f"\nID Number: {id_number} | Age: {voter_age} | Registered: {registered} | Voted: {voted}\n")

  answer = loopcontrol()

  clear()

#end of program - final output displays
#Once the user is ﬁnished entering voters the program should display the final totals
print("\n~~~Below are the totals for the potential voters~~~\n ")
print(f"Not Eligible to Register:  {total_not_eligible_to_register}")
print(f"Of age but not Registered: {total_old_enough_not_registered}")
print(f"Eligible but didn't Vote:  {total_eligible_did_not_vote}")
print(f"Total number of Voters:    {total_voters}")
print(f"Total Records Processed:   {total_records_processed}")

print("\nThank you for using the Voter Analysis Tool. Goodbye :]\n")