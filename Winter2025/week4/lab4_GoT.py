#Ken Pierson
#SE126.04
#W4D2 Lab 4
#1-28-2025

#PROGRAM PROMPT: PART 1 - Write a program that utilizes the got_emails.csv file. Store the file data into 1D parallel lists, then use the information in the lists to assign additional data to each employee. Use the tables below to assign each employee in the file a unique email address, a department, and a unique phone extension. 
# PART 2 - Once you have completed populating all eight parallel lists and displaying the five required back to the user (and in the same Python file), create and write the following data for each employee to a file named westeros.csv: first name, last name, email, department, and phone extension. NOTE: each employee’s data should be on its own record (row) within the newly created file. You will most likely end up with an extra empty line at the end of the file (this is okay for this lab as we will not be reprocessing the data found in this new file). Once the file is ready, close it and alert the user via a displayed message. Also tell them how many employees are in the file, and the total count of employees for each department.

#--IMPORTS---------------------------------------------
import csv
#--FUNCITONS-------------------------------------------

#--MAIN EXECUTING CODE---------------------------------

#initialize a variable

#create an empty list for every potential field in the file
first_name = []
last_name = []
age = []
screen_name = []
house_alleg = []
email = []
dept = ["Research & Development", "Marketing", "Human Resources", "Accounting", "Sales", "Auditing"]
phone_ext = list(range(100,199))

#connecting to the file
with open("text_files/got_emails.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        first_name.append(rec[0])
        last_name.append(rec[1])
        age.append(rec[2])
        screen_name.append(rec[3])
        house_alleg.append(rec[4])
              
#disconnect from file-----------------------------------
for i in range(0, len(screen_name)):
    conv_email = screen_name[i] + "@westeros.net"
    email.append(conv_email)
for i in range(0, len(house_alleg)):
    if house_alleg[i] == "House Stark":
        house_alleg[i] = dept[0]
    if house_alleg[i] == "House Targaryen":
        house_alleg[i] = dept[1]
    if house_alleg[i] == "House Tully":
        house_alleg[i] = dept[2]
    if house_alleg[i] == "House Lannister":
        house_alleg[i] = dept[3]
    if house_alleg[i] == "House Baratheon":
        house_alleg[i] = dept[4]
    if house_alleg[i] == "The Night's Watch":
        house_alleg[i] = dept[5]
    
#print field headers for disply below
print(f"\n{"FIRST":8}    {"LAST":10}     {"EMAIL":30}  {"DEPARTMENT":23}  {"EXT":3}")
print("-" * 90)
#processing through list for display
for i in range(0, len(first_name)):
    print(f"{first_name[i]:10}  {last_name[i]:10}     {email[i]:30}  {house_alleg[i]}")
print("-" * 90)
print(f"Total Number in file: {len(first_name)}\n")
print("-" * 90)
print(phone_ext[0])