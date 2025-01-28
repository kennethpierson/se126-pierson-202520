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
    print("~Search Menu~")
    print("1. Search by LAST Name")
    print("2. Search by FIRST Name")
    print("3. Search by LETTER Grade")
    print("4. Exit")
    #gain search type
    search_type = input("Enter you search type [1-4]: ")
    #filter search options based on type
    if search_type == "1":  #LAST Name
        print()
    elif search_type == "2":  #FIRST Name
        print()
    elif search_type == "3": #LETTER Grade
        print()
    #build a way out of the loop - answer should be able to change value!
    if search_type == "1" or search_type == "2" or search_type == "3":
        answer = loopcontrol()
print("\nThanks for searching good bye!\n")
