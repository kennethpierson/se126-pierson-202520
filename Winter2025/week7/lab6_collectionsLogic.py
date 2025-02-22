#Ken Pierson
#SE126.04
#Lab 6 Collections & Logic
#2-22-2025

#PROGRAM PROMPT: Use lists to create the airplane seating chart - either 1D or 2D lists. You may either create a file to read the data in for the seats, or you can hand-populate your own 1/2D lists. If you choose to create your own file, please upload along with your completed Lab #6 .py file. 


#variable dictionary

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

#--MAIN EXECUTING CODE---------------------------------
#create an empty list for every potential field in the file