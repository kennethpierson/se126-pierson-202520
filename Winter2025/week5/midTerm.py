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
#res_dev            Counting variable for research and development department
#mktg               Counting variable for marketing department
#hr                 Counting variable for human resources department
#acctg              Counting variable for accounting department
#sales              Counting variable for sales department
#audit              Counting variable for auditing department
#first_name         List for firstnames
#last_name          List for lastnames
#age                List for ages
#screen_name        List for screennames
#house_alleg        List for house allegience
#email              List for email addresses
#dept               List for all the departments
#dept_ext           List for the phone extentions of the different departments
#dept_counter       List to used to increment phone ext
#phone_ext          List for the phone ext
#conv_email         create the email by combining screen name with @westeros.net 

#--IMPORTS---------------------------------------------
import csv
#--MAIN EXECUTING CODE---------------------------------

#initialize a variable
res_dev = 0
mktg = 0
hr = 0
acctg = 0
sales = 0
audit = 0

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
        first_name.append(rec[0])
        last_name.append(rec[1])
        email.append(rec[2])
        dept.append(rec[3])
        phone_ext.append(rec[4])
        office.append(office_num[0] + office_count[0])
        office_count[0] += 1 

#disconnect from file-----------------------------------

#print field headers for disply below
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
