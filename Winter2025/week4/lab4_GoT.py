#Ken Pierson
#SE126.04
#W4D2 Lab 4
#1-28-2025

#PROGRAM PROMPT: PART 1 - Write a program that utilizes the got_emails.csv file. Store the file data into 1D parallel lists, then use the information in the lists to assign additional data to each employee. Use the tables below to assign each employee in the file a unique email address, a department, and a unique phone extension. 
# PART 2 - Once you have completed populating all eight parallel lists and displaying the five required back to the user (and in the same Python file), create and write the following data for each employee to a file named westeros.csv: first name, last name, email, department, and phone extension. NOTE: each employee’s data should be on its own record (row) within the newly created file. You will most likely end up with an extra empty line at the end of the file (this is okay for this lab as we will not be reprocessing the data found in this new file). Once the file is ready, close it and alert the user via a displayed message. Also tell them how many employees are in the file, and the total count of employees for each department.

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
age = []
screen_name = []
house_alleg = []
email = []
phone_ext = []
#create lists that hold specific values
dept = ["Research & Development", "Marketing", "Human Resources", "Accounting", "Sales", "Auditing"]
dept_ext = [100,200,300,400,500,600]
dept_counter = [0, 0, 0, 0, 0, 0]

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