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

#connecting to the file----------------------------------
with open("text_files/got_emails.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        first_name.append(rec[0])
        last_name.append(rec[1])
        age.append(rec[2])
        screen_name.append(rec[3])
        house_alleg.append(rec[4])

#disconnect from file-----------------------------------

for i in range(0, len(screen_name)):                            #for loop to create the email addresses
    conv_email = screen_name[i] + "@westeros.net"
    email.append(conv_email)
for i in range(0, len(house_alleg)):                            #for loop for the departments and phone extentions
    if house_alleg[i] == "House Stark":                         
        house_alleg[i] = dept[0]                                #takes the house allegiance and matches it to the department
        phone_ext.append(dept_ext[0] + dept_counter[0])         #creates a unique phone ext within the dept range
        dept_counter[0] += 1                                    #increments by one each time so different extensions are handed out
        res_dev += 1                                            #used to count the number of employees in this particular department
    if house_alleg[i] == "House Targaryen":
        house_alleg[i] = dept[1]
        phone_ext.append(dept_ext[1] + dept_counter[1])
        dept_counter[1] += 1
        mktg += 1
    if house_alleg[i] == "House Tully":
        house_alleg[i] = dept[2]
        phone_ext.append(dept_ext[2] + dept_counter[2])
        dept_counter[2] += 1
        hr += 1
    if house_alleg[i] == "House Lannister":
        house_alleg[i] = dept[3]
        phone_ext.append(dept_ext[3] + dept_counter[3])
        dept_counter[3] += 1
        acctg += 1
    if house_alleg[i] == "House Baratheon":
        house_alleg[i] = dept[4]
        phone_ext.append(dept_ext[4] + dept_counter[4])
        dept_counter[4] += 1
        sales += 1
    if house_alleg[i] == "The Night's Watch":
        house_alleg[i] = dept[5]
        phone_ext.append(dept_ext[5] + dept_counter[5])
        dept_counter[5] += 1
        audit += 1

#print field headers for disply below
print(f"\n{"FIRST":8}    {"LAST":10}     {"EMAIL":30}  {"DEPARTMENT":23}  {"EXT":3}")
print("-" * 90)
#processing through list for display
for i in range(0, len(first_name)):
    print(f"{first_name[i]:10}  {last_name[i]:10}     {email[i]:30}  {house_alleg[i]:23}  x{phone_ext[i]}")
print("-" * 90)

#create and write westeros.csv
file = open("text_files/westeros.csv", "w")
for i in range(0, len(first_name)):
    file.write(f"{first_name[i]},{last_name[i]:},{email[i]},{house_alleg[i]},{phone_ext[i]}\n")
file.close()
#final output display
print(f"\nThe file has been created and saved to the following: text_files/westeros.csv \n")
print("--------- Department Totals ----------")
print(f"Employees in Research & Development: {res_dev}")
print(f"Employees in Marketing:              {mktg}")
print(f"Employees in Human Resources:        {hr}")
print(f"Employees in Account:                {acctg}")
print(f"Employees in Sales:                  {sales}")
print(f"Employees in Auditing:               {audit}")
print("-" * 90)
print(f"Total Number of Employees:          {len(first_name)}")
print("\nThank you for using the program. Goodbye.\n")