#w8D2 - Dictionary Review + Gaining data from text files
#this demo utilizes: dictionary_file.csv

#---IMPORTS---------------------------------------------------------------------
import csv
#---MAIN EXECUTING CODE---------------------------------------------------------
library = {
    #"key" : value
    "1230" : "Red Rising",
    "1231" : "The Little Prince"
}

with open("text_files/dictionary_file.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        #for every record in the file, do the following
        #file --> 2D list; rec --> 1 record's data, also a list!
        library.update({rec[0] : rec[1]})
        #library_num --> rec[0], a string
        #title --> rec[1], also string

#---DISCONNECT FROM FILE---------------------------------------------------------

print(f"{"KEY":4} : {"TITLE"}")
print("-" * 50)
for key in library:
    #for every key found in the library dictionary
    print(f"{key:4} : {library[key]}")
print("-" * 50)

#---SEQUENTIAL SERCH with DICTIONARIES--------------------------------------------
search = input("\nEnter the Title you are looking for: ")

found = 0

for key in library:
    if search.lower() == library[key].lower():
        found = key

if found != 0:
    print(f"We found your search for {search}, here is the info:\n ")
    print(f"{"KEY":4} : {"TITLE"}")
    print("-" * 50)
    '''
    for i in range(0. len(found)):
        print(f"{found[i]:4} : {library[found[i]]}")
    '''
    print(f"{found:4} : {library[found]}")
    print("-" * 50)
else:
    print(f"We could not find your search for {search}")

search = input("\nEnter the Library number you are looking for: ")

found = 0

for key in library:
    if search.lower() == key.lower():
        found = key

if found != 0:
    print(f"We found your search for {search}, here is the info:\n ")
    print(f"{"KEY":4} : {"TITLE"}")
    print("-" * 50)
    print(f"{found:4} : {library[found]}")
    print("-" * 50)
else:
    print(f"We could not find your search for {search}")