#W4D1 - Sequential Search

#PROMPT: We will continue to work with the class_grades.csv file, as used in the W3D2 demo. We will practice connecting to a file, storing the file data into parallel lists, and creating new data for each student record based on these lists. We will then build a sequential search program which will allow us to find students in the file, and write data regarding them to a newly created file in our repository.

#this file uses: class_grade.csv

#--IMPORTS--------------------------------------------------------------------
import csv
#--FUNCTIONS------------------------------------------------------------------
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

#--MAIN EXECUTING CODE--------------------------------------------------------

#create some empty lists - one list for every potential filed in the file
firstName =[]
lastName = []
test1 = []
test2 = []
test3 = []

#connecting to the file
with open("text_files/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)

    for record in file:   
        #store date from current record to corresponding lists (each field is its own!)
        #.append() --> adds the data to the next available space in the list (end)

        #parallel lists --> data dispersed across lists, connected by the same index
        firstName.append(record[0])
        lastName.append(record[1])
        test1.append(int(record[2]))
        test2.append(int(record[3]))
        test3.append(int(record[4])) 

#disconnect from file------------------------------------------------------------------------

#process the lists to create and store each student's numeric average as well as letter grade average, then display all data back to the user

num_avg = []  #holds student's numeric avg: (test1 + test2 + test3) /3
let_avg = []  #holds student's letter avg: letter(num_avg) return

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

#sequential search - search for a student by their last name

#step 1: set-up and gain search query
found = -1 #flag var, will be replaced with index position if name is found
search_last = input("Enter the last name you wish to find: ") #name we are looking for

#step 2: perform search also (seq. search - > for loop w/ if statement) 
for i in range(0, len(lastName)):
    #for loop performs the SEQUENCE - from start through end of list items

    if search_last.lower() == lastName[i].lower():
        #if performs the SEARCH - is what we're looking for here in the list?
        found = i  #stores found intem's INDEX LOCATION

#step 3: display results to user; make sure you give info: both for found or NOT found
if found != -1:
    #last name found
    print(f"Your search for {search_last.title()} was FOUND! Here is their data:\n")
    print(f"{"FIRST":10}  {"LAST":10}  {"T1":3}  {"T2":3}  {"T3":3}  {"# AVG":6}  {"L AVG"}")
    print("-" * 55)
    print(f"{firstName[found]:10}  {lastName[found]:10} {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {num_avg[found]:6.1f}   {let_avg[found]}\n")
else:
    #NOT Found
    print(f"Your search for {search_last.title()} was NOT FOUND!")
    print("Check your cAsInG and sPeLlInG and try again!\n")

print("-" * 38)
print("Welcome to the Student Search Program")
answer = input("Would you like to start your search? [y/n]: ").lower()
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
        answer = input("Would you like to search again? [y/n]: ").lower()
print("Thanks for searching good bye!")