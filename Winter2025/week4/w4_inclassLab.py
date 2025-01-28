#Ken Pierson
#SE126.04
#W4D1 In Class Lab
#1-27-2025

#PROGRAM PROMPT: Part 1 - Write a program that reads the data file (below) and stores the data into 1D parallel lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file.
#Part 2 - Next, reprocess the lists to find each student's current average score, letter grade equivalent, and the class average.  While processing in the for loop, store each student's average into a new list called 'num_avg' and their letter grade into a list called 'let_avg'. Then, print each student's full information, record by record including average score and average letter equivalent.  After this print of the original file data from the lists, print to the console the total number of student's in the class along with the class numeric average.  
#Part 3 - After your final display using the 1D parallel lists, create a sequential search program which allows the user to repeatedly utilize the following menu of search types. When a searched for item is found, display all student data to the console. When a search is compete and no matching data is found, alert the user. Search options 1 and 2 should only show one found student, where search option 3 should show a potential of multiple students.

#VARIABLE DICTIONARY:

#--IMPORTS---------------------------------------------
import csv
#--FUNCITONS-------------------------------------------
def letter(num):
    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:
        let = "F"
    else:
        let = "ERROR"
    return let #the "let" value will literally replace the letter() call in main code

def loopcontrol(): #() is empty so NO parameters; this function does not require any info to run
  ans = input("Would you like to search again? [y/n]: ").lower()
  #check the ans value, repeat back to user if necessary
  while ans != "y" and ans != "n":
    print("***INVALID ENTRY***")
    ans = input("Would you like to search again? [y/n]: ").lower()
  #return the ans value tp be used in the base program!
  return ans

#--MAIN EXECUTING CODE---------------------------------

#create an empty list for every potential field in the file
firstName =[]
lastName = []
test1 = []
test2 = []
test3 = []
num_avg = []  #holds student's numeric avg: (test1 + test2 + test3) /3
let_avg = []  #holds student's letter avg: letter(num_avg) return

#connecting to the file
with open("text_files/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)

    for record in file:   
        #parallel lists --> data dispersed across lists, connected by the same index
        firstName.append(record[0])
        lastName.append(record[1])
        test1.append(int(record[2]))
        test2.append(int(record[3]))
        test3.append(int(record[4])) 

#disconnect from file-----------------------------------

#print field headers for disply below
print(f"\n{"FIRST":10}  {"LAST":10}   {"T1":3}  {"T2":3}  {"T3"}")
print("-" * 40)
#processing through list for display
for i in range(0, len(firstName)):
    print(f"{firstName[i]:10}  {lastName[i]:10}  {test1[i]:3}  {test2[i]:3}   {test3[i]}")
print("-" * 40)
print(f"Total Students in file: {len(firstName)}\n")
print("-" * 55)

for i in range(0, len(firstName)):
    a = (test1[i] + test2[i] + test3[i]) / 3
    num_avg.append(a)
    let_avg.append(letter(a))

#print field headers for disply below
print(f"\n{"FIRST":10}  {"LAST":10}   {"T1":3}  {"T2":3}  {"T3":3}  {"# AVG":6}  {"L AVG"}")
print("-" * 55)
#processing through list for display
for i in range(0, len(firstName)):
    print(f"{firstName[i]:10}  {lastName[i]:10}  {test1[i]:3}  {test2[i]:3}  {test3[i]:3}  {num_avg[i]:6.1f}    {let_avg[i]}")
print("-" * 55)
print(f"Total Students in file: {len(firstName)}\n")
print("-" * 55)

print("Welcome to the Student Search Program")
#answer = input("Would you like to start your search? [y/n]: ").lower()
answer = "y"
while answer == "y":
    #show user search menu
    print("\t~Search Menu~")
    print("1. Search by LAST Name")
    print("2. Search by FIRST Name")
    print("3. Search by LETTER Grade")
    print("4. Exit")
    #gain search type
    search_type = input("Enter you search type [1-4]: ")
    print()
    #filter search options based on type
    if search_type == "1": #LAST NAME
        #sequential search - search for a student by their LAST name
        #this version of sequential search is looking for ONE item, a specific and unique LAST name
        
        print("\t~LAST NAME SEARCH~")
        #step 1: set-up and gain search query
        found = -1  #flag var, will be replaced with index position if name is found; we are using a -1 because it is not a valid index location
        search_last = input("Enter the last name you wish to find: ") #name we are looking for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(lastName)):
            #for loop performs the SEQUENCE - from start through end of list items

            if search_last.lower() == lastName[i].lower(): 
                #if performs the SEARCH - is what we're looking for here in the list?
                found = i  #stores found item's INDEX LOCATION

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if found != -1:
            #last name FOUND!
            print(f"Your search for {search_last.title()} was FOUND! Here is their data:\n ")
            print(f"{"FIRST":10}  {"LAST":10}   {"T1":3}  {"T2":3}  {"T3":3}  {"# AVG":6}  {"L AVG"}")
            print(f"{firstName[found]:10}  {lastName[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {num_avg[found]:6.1f}   {let_avg[found]}\n")
        else: 
            #NOT found
            print(f"Your search for {search_last.title()} was NOT FOUND!")
            print("Check your spelling and try again!")

    elif search_type == "2": #FIRST NAME
        #sequential search - search for a student by their LAST name
        #this version of sequential search is looking for ONE item, a specific and unique LAST name
        
        print("\t~FIRST NAME SEARCH~")
        #step 1: set-up and gain search query
        found = -1  #flag var, will be replaced with index position if name is found; we are using a -1 because it is not a valid index location
        search_first = input("Enter the first name you wish to find: ") #name we are looking for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(firstName)):
            #for loop performs the SEQUENCE - from start through end of list items

            if search_first.lower() == firstName[i].lower(): 
                #if performs the SEARCH - is what we're looking for here in the list?
                found = i  #stores found item's INDEX LOCATION

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if found != -1:
            #last name FOUND!
            print(f"Your search for {search_first.title()} was FOUND! Here is their data: ")
            print(f"\n{"FIRST":10}  {"LAST":10}   {"T1":3}  {"T2":3}  {"T3":3}  {"# AVG":6}  {"L AVG"}")
            print(f"{firstName[found]:10}  {lastName[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {num_avg[found]:6.1f}   {let_avg[found]}")
        else: 
            #NOT found
            print(f"Your search for {search_first.title()} was NOT FOUND!")
            print("Check your spelling and try again!")
    
    elif search_type == "3": #LETTER GRADE
        print("\tLETTER GRADE SEARCH")

        #sequential search - search for a collection of students based on their Letter Grade Average
        #this version of sequential search is looking for MULTIPLE items, based on a specific letter grade

        #step 1: set-up and gain search query
        found = []  #empty list, found locations (index) will be stored if/when found
        search_let= input("Enter the LETTER GRADE you wish to find: ") #grade we are looking through all students for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(let_avg)):
            #for loop performs the SEQUENCE - from start through end of list items

            if search_let.upper() == let_avg[i]: 
                #if performs the SEARCH - is what we're looking for here in the list?
                found.append(i)  #stores found item's INDEX LOCATION to the found list because we may have multiple students whose letter grade fits the searched for grade
                #print(f"Found a {search_let} grade in INDEX {i}")

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if not found: #'if not found' means 'found' is an EMPTY LIST
            #NOT found
            print(f"Your search for {search_let.upper()} was NOT FOUND!")
            print("Please try again!")
        else: 
            #last name FOUND!
            print(f"Your search for {search_let.upper()} was FOUND! Here is their data: ")
            print(f"\n{"INDEX":8} {"FIRST":10}  {"LAST":10}   {"T1":3}  {"T2":3}  {"T3":3}  {"# AVG":6}  {"L AVG"}")
            #'found' is a list populated with index locations - we loop through this list, and use found[i] (which again, holds an INDEX from our other searched-through list) to be recalled and used below
            for i in range(0, len(found)):
                print(f"{found[i]:3}:     {firstName[found[i]]:10}  {lastName[found[i]]:10}  {test1[found[i]]:3}  {test2[found[i]]:3}  {test3[found[i]]:3} {num_avg[found[i]]:6.1f}    {let_avg[found[i]]}")
    elif search_type == "4": #exit
        print("\t~EXIT~")
        answer = "x"
    else:
        print("\t!INVALID ENTRY!")
    #build a way out of the loop - answer should be able to change value!
    if search_type == "1" or search_type == "2" or search_type == "3":
        answer = loopcontrol()
print("\nThanks for searching good bye!\n")