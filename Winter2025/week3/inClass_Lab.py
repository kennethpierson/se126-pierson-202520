#Ken Pierson
#SE126.04
#W3D1 In Class Lab
#1-19-2025

#PROGRAM PROMPT:  Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.

#VARIABLE DICTIONARY:
#total_computers    initializes the variable
#file               variable for the csv file
#type               variable for the type of computer
#full_type          used for when the type variable is converted to the full word
#brand              variable for the computer brand
#full_brand         used for when the brand variable is converted to the full word
#cpu                variable for the computer cpu
#ram                variable for the computer ram
#disk_1             variable for the computer 1st hard drive
#num_hd             variable for the number of hard drives in the computer
#disk_2             variable for the computer 2nd hard drive if it has one
#op_sys             variable for the computer operating system
#year               variable for year the computer was purchased

#--IMPORTS---------------------------------------------
import csv

#--FUNCITONS-------------------------------------------
#this function converts D to Desktop and L to Laptop
def modify_type(ty):
    if ty == "D":
        return "Desktop"
    if ty == "L":
        return "Laptop"

#This function converts the brand from an abbriviation
def modify_brand(bnd):
    if bnd == "DL":
        return "Dell"
    elif bnd == "GW":
        return "Gateway"
    else:
        return "HP"
    
#--MAIN EXECUTING CODE---------------------------------

#create empty list for every potential field in the file
type = []            #computer type Desktop or Laptop
full_type = []
brand = []           #for the computer manufacturer
full_brand = []
cpu = []             #processor type
ram = []             #total ram
disk_1 = []          #hard drive one
num_hd = []          #number of hard drives
disk_2 = []          #hard drive two
op_sys = []          #operating system
year = []            #year the machine was purchased



#initialize the counting variables
total_computers = 0 

print(f"\n{"Type":10}  {"Brand":8}  {"CPU":3}  {"RAM":2}  {"1st Disk":5}  {"No HDD":2}  {"2nd Disk":10}  {"OS":3}  {"YR":2}")

#-----connected to file--------
with open("text_files/filehandling.csv") as csvfile:

    file = csv.reader(csvfile)

    for record in file:
        total_computers += 1
        #takes the information out of the file and stores it
        type = record[0]
        #calls the function
        full_type.append(modify_type(type))
        brand = record[1]         
        full_brand.append(modify_brand(brand))
        cpu.append(record[2])
        ram.append(int(record[3]))
        disk_1.append(record[4])
        num_hd.append(int(record[5]))
        #Looks at the number of hard drives and pulls the information from the correct column
        if num_hd == 1:
            op_sys.append(record[6])
            year.append(record[7])
            print(f"{full_type:10}  {full_brand:8}  {cpu:2}  {ram:4}  {disk_1:2}  {num_hd:9}              {op_sys:2}  {year} ")
        if num_hd == 2:
            disk_2.append(record[6])
            op_sys.append(record[7])
            year.append(record[8])
            print(f"{full_type:10}  {full_brand:8}  {cpu:2}  {ram:4}  {disk_1:2}  {num_hd:9}  {disk_2:10}  {op_sys:2}  {year} ")
               
#-----Final Output--------        
print("-----------------------------------------------------------")
print(f"\nThere are {total_computers} computers in the file.")
print("\nThank you for using the program. Goodbye.\n")