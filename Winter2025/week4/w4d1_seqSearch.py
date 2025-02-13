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

'''
A simple overview of sequential search:

#step 1: set up and gain search
found = -1 #we are using -1 because it is not a valid index location (technically); you could also use found = "x"

search = input("What are you searching for? ")

#step 2: perform the searching algorithm
for i in range(0, len(listYouAreSearchingThrough)):

    if search == listYouAreSearchingThrough[i]: 
        found = i #found drops its original value (-1 or "x") and is replaced with the current index location
        #since this occurs in the if statement, it will only happen IF what we are looking for matches one of the values on the list we are searching through

#step 3: check and display your results
if found != -1: #(or "x" if that was your initial value
    #found has changed, meaning at some point it checked into the if statement within our searching for loop
    
    print(f"Your search for {search} has been FOUND!")
    #display relevant data/results here using 'found' as your index representer 
    print(f"{listYouAreSearchingThrough[found]}")
    
else:
    #found is still its initial value, meaning we did not find the data the user was looking for
    #tell the user their search came up empty
    print(f"Your search for {search} has NOT BEEN FOUND!")

'''
