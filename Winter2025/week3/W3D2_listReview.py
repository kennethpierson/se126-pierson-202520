#W3D2 - List Review - 1Dimensional Lists & Parallel Lists

#PROMPT: Our W3D2 demo will focus on reviewing accessing text file data and storing the data into 1D lists. We will store the file data into respective lists, then process the data to print the information for each student as well as calculate and store a new piece of data for each student: their current average test score.

#this file uses: class_grade.csv

#--IMPORTS--------------------------------------------------------------------
import csv
#--FUNCTIONS------------------------------------------------------------------

#--MAIN EXECUTING CODE--------------------------------------------------------

#initialize a record counting variable
total_record = 0

#create an empty list for every potential field in the file
firstName =[]
lastName = []
test1 = []
test2 = []
test3 = []

#connecting to the file
with open("text_files/class_grades.csv") as csvfile:

    file = csv.reader(csvfile)

    for record in file:

        total_record += 1
        
        #store date from current record to corresponding lists (each field is its own!)
        #.append() --> adds the data to the next available space in the list (end)

        #parallel lists --> data dispersed across lists, connected by the same index
        firstName.append(record[0])
        lastName.append(record[1])
        test1.append(int(record[2]))
        test2.append(int(record[3]))
        test3.append(int(record[4]))

#disconnected from file

#processing lists -- USE A FOR LOOP
for index in range(0,  len(firstName)):
    ##for every item, index will start at 0 and run up to (not including) the length (# of items)
    print(f"INDEX {index}: {firstName[index]:10}  {lastName[index]:10}  {test1[index]:3}  {test2[index]:3}  {test3[index]:3}")

#create a new list to hold each student's average test score

avg = []

for i in range(0, len(test1)):

    a = (test1[i] + test2[i] + test3[i]) / 3
    avg.append(a)

print(f"INDEX #: {"FIRST":10}  {"LAST":10}  {"TEST1":3}  {"TEST2":3}  {"TEST3":3}  {"AVG"}")
print("-" * 80)
for index in range(0,  len(firstName)):
    ##for every item, index will start at 0 and run up to (not including) the length (# of items)
    print(f"INDEX {index:3}: {firstName[index]:10}  {lastName[index]:10}  {test1[index]:3}  {test2[index]:3}  {test3[index]:3}  {avg[index]:.2f}")
print("-" * 80)

#calculate the entire class avg using a for loop to add each students's avg to the class total
total_avg = 0
for i in range(0, len(avg)):
    total_avg += avg[i]

class_avg = total_avg / len(avg)

print(f"\nTotal Record: {total_record}")
print(f"Current Class Average: {class_avg:.2f}")
print(f"GoodBye!\n")