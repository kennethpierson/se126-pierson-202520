#W4D2 - Sequential Search Review + Creating & writing to Text Files

#PROGRAM PROMPT: In the W4D2 demo, we will review utilizing sequential search for simple singular and multi returns. We will then create and write data to a text file using Python.

#--IMPORTS---------------------------------------------
import csv
#--FUNCTIONS-------------------------------------------

#--MAIN EXECUTING CODE---------------------------------

#create empty lists - one list for every potential filed in the file
dragons = []    #field0
riders = []     #field1
count = []      #field2
color1 = []     #field3
color2 = []     #field4

with open("text_files/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        dragons.append(rec[0])
        riders.append(rec[1])
        count.append(rec[2])
        color1.append(rec[3])

        if rec[2] == "2":
            color2.append(rec[4])
        else:
            color2.append("---")
        

#disconnected from file -------------------------

#process the list to displat data at console
print(f"{"Dragons":15} {"Riders":30} {"#":3} {"Color1":8} {"Color2":8}")
for i in range(0, len(dragons)):
    print(f"{dragons[i]:15} {riders[i]:30} {count[i]:3} {color1[i]:8} {color2[i]}")

#Search for a Specific Dragon
#step1: set-up and gain of search
found = "x"
search = input("Which dragon are you looking for: ")

#step 2: perform search --> for loop w if statement
for i in range(0, len(dragons)):
    if search.lower() in dragons[i].lower():
        #hold onto the found location of our searched for value
        found = i

#step 3: filter and display resualts
if found != "x":
    print(f"Your search for {search} was FOUND:")
    print (f"{dragons[found]:15} {riders[found]:30} {count[found]:3} {color1[found]:8} {color2[found]:8}")
else:
    print(f"Your search for {search} was not found:")

#search for color set

found = []
search = input("Enter the dragon color you are looking for:")

for i in range(0, len(color1)):
    if search.lower() in color1[i] or search.lower() in color2[i]:
        found.append(i)
    
if not found:
    print(f"Your search for {search} was not found:")
else:
    print(f"Your search for {search} was found:")
    for i in range(0, len(found)):
        print (f"{dragons[found[i]]:15} {riders[found[i]]:30} {count[found[i]]:3} {color1[found[i]]:8} {color2[found[i]]:8}")

#write some data to a new file
#create and write all of the data to a new text file
file = open("text_files/test.csv", "w")
file.write("Hello World!")
file.close()

#create and write dragons and riders
file = open("text_files/D_R.csv", "w")
for i in range(0, len (dragons)):
    file.write(f"{dragons[i]},{riders[i]}\n")
file.close()
