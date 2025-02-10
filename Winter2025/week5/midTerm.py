#Ken Pierson
#SE126.04
#MidTerm Choice 1
#2-10-2025

#PROGRAM PROMPT: Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have been fully populated with file data, create a new list to hold an office number for each of the employees. Office numbers should start at 100 and not exceed 200. Assign each employee an office number and store to the newly created list, then process through the six lists to display all of the data to the user as well as the total number of records in the file. Once all of the data has been displayed, write all of the list data to a new file called ‘midterm_choice1.csv’, where each employee’s information is found on one record in the file and their data is separated by a comma (additional empty line in resulting file is okay). Finally, create a sequential search program that allows a user to repeatedly search the employee information stored in the lists based on the following menu: 
# Westeros Services Directory Search 
#1.	Search by EMAIL
#2.	Search by DEPARTMENT
#3.	EXIT 

#variable dictionary
#first_name         List for firstnames
#last_name          List for lastnames
#email              List for email addresses
#dept               List for all the departments
#phone_ext          List for the phone ext
#office             List for the office number
#office_num         List for the starting point of the office numbers
#office_count       List use to increment the office number
#search_type        for the menu options
#search_email       for the email search
#search_dept        for the department search

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
#--MAIN EXECUTING CODE---------------------------------

#create an empty list for every potential field in the file
first_name = []
last_name = []
email = []
dept = []
phone_ext = []
office =[]
office_num = [100]
office_count = [0]

#connecting to the file----------------------------------
with open("text_files/westeros.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #parallel lists --> data dispersed across lists, connected by the same index
        first_name.append(rec[0])
        last_name.append(rec[1])
        email.append(rec[2])
        dept.append(rec[3])
        phone_ext.append(rec[4])
        office.append(office_num[0] + office_count[0])
        office_count[0] += 1 

#disconnect from file-----------------------------------

#print field headers for display below
print(f"\n{"FIRST":8}    {"LAST":10}     {"EMAIL":30}  {"DEPARTMENT":23}  {"EXT":4}    {"Office"} ")
print("-" * 100)
#processing through list for display
for i in range(0, len(first_name)):
    print(f"{first_name[i]:10}  {last_name[i]:10}     {email[i]:30}  {dept[i]:23}  x{phone_ext[i]:4}   {office[i]}")
print("-" * 100)
print(f"\nTotal Number of Employees: {len(first_name)}\n")

#create and write westeros.csv
file = open("text_files/midterm_choice1.csv", "w")
for i in range(0, len(first_name)):
    file.write(f"{first_name[i]},{last_name[i]},{email[i]},{dept[i]},{phone_ext[i]},{office[i]}\n") 
file.close()

print("Westeros Services Directory Search ")
answer = "y"
while answer == "y":
    #show user search menu
    print("-------Search Menu-------")
    print("1. Search by Email")
    print("2. Search by Department")
    print("3. Exit")
    #gain search type
    search_type = input("Enter you search type [1-3]: ")
    print()

    if search_type == "1":               
        print("------- Email Search -------")
        #step 1: set-up and gain search query
        found = "x"  #flag var, will be replaced with index position if name is found
        search_email = input("Enter the email you wish to find: ") #email we are looking for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(email)):
            #for loop performs the SEQUENCE - from start through end of list items
            if search_email.lower() == email[i].lower(): 
                found = i  #stores found item's INDEX LOCATION

       #step 3: display results to user; make sure you give info: both for found or NOT found
        if found != "x":      
            #Email FOUND!
            print(f"Your search for {search_email} was FOUND! Here is their data:\n ")
            print(f"{"FIRST":8}    {"LAST":10}     {"EMAIL":30}  {"DEPARTMENT":23}  {"EXT":4}    {"Office"} ")
            print(f"{first_name[found]:10}  {last_name[found]:10}     {email[found]:30}  {dept[found]:23}  x{phone_ext[found]:4}   {office[found]}\n")
        else:
            #Email NOT FOUND!
            print(f"Your search for {search_email} was NOT FOUND!")
            print("Please try again!")

    elif search_type == "2": #Department
        #sequential search - search for Empolyee's Department
                
        print("------- Department Search -------")
        #step 1: set-up and gain search query
        found = [] 
        search_dept = input("Enter the Department you wish to find: ") #Department we are looking for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(dept)):
            #for loop performs the SEQUENCE - from start through end of list items
            if search_dept.lower() == dept[i].lower(): 
                found.append(i)   #stores found item's INDEX LOCATION

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if not found: #'if not found' means 'found' is an EMPTY LIST
            #NOT found
            print(f"Your search for {search_dept} was NOT FOUND!")
            print("Please try again!")
        else: 
           #departmet found
           print(f"Your search for {search_dept.title()} was FOUND! Here is their data: ")
           print(f"\n{"FIRST":8}    {"LAST":10}     {"EMAIL":30}  {"DEPARTMENT":23}  {"EXT":4}    {"Office"} ")
           for i in range(0, len(found)):
               print(f"{first_name[found[i]]:10}  {last_name[found[i]]:10}     {email[found[i]]:30}  {dept[found[i]]:23}  x{phone_ext[found[i]]:4}   {office[found[i]]}")
    elif search_type == "3": #exit
        print("\t---EXIT---")
        answer = "x"
    else:
        print("\t!INVALID ENTRY!")
    #build a way out of the loop - answer should be able to change value!
    if search_type == "1" or search_type == "2":
        answer = loopcontrol()
print("\nThank You for using the Program! Good Bye!\n")