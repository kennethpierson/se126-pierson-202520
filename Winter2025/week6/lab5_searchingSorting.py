#Ken Pierson
#SE126.04
#Lab 5 Searching & Sorting
#2-15-2025

#PROGRAM PROMPT: Build a personal library search system using the file book_list.csv. Store the file data into 1D parallel lists, then use the appropriate searching algorithms for the menu system options.  Your program should give your user the following menu:
#Personal Library Menu
#1.	Show All Titles – list all book data to the user alphabetically by title
#2.	Search by Title – allow for an entire title or a title key word
#3.	Search by Author – show all titles of the searched-for author
#4.	Search by Genre - show all titles of the searched-for genre
#5.	Search by Library Number – only allow for one specific library number item
#6.	Show All Available – show all titles with status “available”
#7.	Show All On Loan - show all titles with status “on loan”
#8.	EXIT
#When your user runs any of the options 1 – 7, show all data associated with the search [Library Number, Title, Author, Genre, Page count, Status]. Do not allow the program to end unless the user chooses option 8 to exit. All searches should not be case sensitive.


#variable dictionary
#library_num     List for library numbers
#title           List for book titles
#author          List for book authors
#genre           List for book genres
#page_count      List for book page counts
#status          List for book status
#found           Used to store variables


#--IMPORTS---------------------------------------------
import csv
#--FUNCITONS-------------------------------------------
def display(x, records):
        #PARAMETERS: x   signifier for if we are printing a single record or multiple
        #when x != "x" it is an integere index and we have one value, otherwise we have multiple
        #records   the length of a list we are going to process through (# of loops/prints)
    print(f"{'Library #':12}  {'Title':35}  {'Author':25}  {'Genre':15}   {'Pages':5}  {'Status'}")
    print("-" * 115)
    if x != "x":
        #printing one record
        print(f"{library_num[x]:12}  {title[x]:35}  {author[x]:25}  {genre[x]:15}   {page_count[x]:5}  {status[x]}")
    elif found:
        #printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{library_num[found[i]]:12}  {title[found[i]]:35}  {author[found[i]]:25}  {genre[found[i]]:15}   {page_count[found[i]]:5}  {status[found[i]]}") 
    else:
        #printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{library_num[i]:12}  {title[i]:35}  {author[i]:25}  {genre[i]:15}   {page_count[i]:5}  {status[i]}")
    print("-" * 115)

def swap(i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp

#--MAIN EXECUTING CODE---------------------------------
#create an empty list for every potential field in the file
library_num = []
title = []
author = []
genre = []
page_count = []
status = []
found = []

#connecting to the file----------------------------------
with open("text_files/book_list.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #parallel lists --> data dispersed across lists, connected by the same index
        library_num.append(rec[0])
        title.append(rec[1])
        author.append(rec[2])
        genre.append(rec[3])
        page_count.append(rec[4])
        status.append(rec[5])

#disconnect from file-----------------------------------
#display whole list data to user
#display("x",len(library_num))

#main searching loop
answer = "y"
while answer == "y":
    found = [] #reset found list so each new menu/search is is empty
    print("\n***Personal Library Menu***")
    print("1. Show All Titles") #list all book data to the user alphabetically by title
    print("2. Show All Available") #show all titles with status “available”
    print("3. Show All On Loan") #show all titles with status “on loan”
    print("4. Search by Title ") #allow for an entire title or a title key word
    print("5. Search by Author") #show all titles of the searched-for author
    print("6. Search by Genre") #show all titles of the searched-for genre
    print("7. Search by Library Number") #only allow for one specific library number item
    print("8. EXIT")

    search_type = input("\nWhat would you like to search today? [1-8]: ")

    #using 'not in' for user validity checks
    if search_type not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
         print("\n***INVALID ENTRY! Please try again***\n")
    elif search_type == "1":
        print(f"\nYou have chosen to Show All Titles")
        #BINARY SEARCH: 
        #               * requires a collection of UNIQUE values to search through
        #               * requires the collection to be SORTED (ORDERED)
        #                       ascending or descending ; alpha or numeric

        #Bubble Sort --> higher values 'bubble' to the bottom of the collection
        #below is sorting for ascending alpha order
        for i in range(0, len(title) -1):
            for j in range(0, len(title) -1):
                if title[j] > title[j + 1]:
                    #they must swap places because the higher value must come afterwards
                    temp = title[j]
                    title[j] = title[j + 1]
                    title[j + 1] = temp

                    #use the function to cut down on coding and potential errors!
                    swap(j, library_num)
                    swap(j, author)
                    swap(j, genre)
                    swap(j, page_count)
                    swap(j, status)

        #check bubble sort --> sorting in ascending order by name
        display("x", len(title)) #call display() to show the values
    
    elif search_type == "2":
        print(f"\nYou have chosen to Show All Available")
        search = "available"
        for i in range(0, len(status)):
            if search == status[i]:
                found.append(i)
        display("x", len(found)) #call display() to show the values

    elif search_type == "3":
        print(f"\nYou have chosen to Show All On Loan")
        search = "on loan"
        for i in range(0, len(status)):
            if search == status[i]:
                found.append(i)
        display("x", len(found)) #call display() to show the values

    elif search_type == "4":
        print(f"\nYou have chosen to search by Title\n")

        search = input("Which Title are you looking for: ").lower()    
        
        #allow the user to search for a KEYWORD within the title[] values

        for i in range(0, len(title)):
            if search.lower() in title[i].lower():
                found.append(i)

        if not found:
            print(f"\nSorry, we could not find your search for {search}. Please try again.")

        else:
            print(f"\nWe have found your search for {search}, see details below:\n")
            display("x", len(found)) #call display() to show the values

    elif search_type == "5":
        print(f"\nYou have chosen to search by Author\n")

        search = input("Which Author are you looking for: ").lower()    

        for i in range(0, len(author)):
            if search.lower() in author[i].lower():
                found.append(i)

        if not found:
            print(f"\nSorry, we could not find your search for {search}. Please try again.")

        else:
            print(f"\nWe have found your search for {search}, see details below:\n")
            display("x", len(found)) #call display() to show the values

    elif search_type == "6":
        print(f"\nYou have chosen to search by Genre\n")

        search = input("Which Genre are you looking for:").lower()    
        
        for i in range(0, len(genre)):
            if search.lower() in genre[i].lower():
                found.append(i)

        if not found:
            print(f"\nSorry, we could not find your search for {search}. Please try again.")

        else:
            print(f"\nWe have found your search for {search}, see details below:")
            display("x", len(found)) #call display() to show the values

    elif search_type == "7":
        print(f"\nYou have chosen to search by Library Number")
        
        search = input("Which Library Number are you looking for:")
        #using 'not in' for user validity checks
        if search not in library_num:
            print("\nSorry, wrong library number, Please try again.")

        else:
            for i in range(0, len(library_num)):
                if search == library_num[i]:
                    found.append(i)

            #display results
            if not found: #if the found list is still empty
                print(f"\nSorry, your serach for {search} came up empty :[")
            else:
                #call display() to show the values
                display("x", len(found))

    elif search_type == "8":
        #exiting output display
        print(f"\nYou are now exiting the program. Thank you for searching!")
        answer = "n"
