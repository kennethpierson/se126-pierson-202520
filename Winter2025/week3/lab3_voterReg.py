#Name Ken Pierson
#W3D2 # Lab 3
#Date January 26, 2025
#SE126.04

#Construct a program that will analyze potential voters. The program should generate the following totals:
#1. Number of individuals not eligible to register.
#2. Number of individuals who are old enough to vote but have not registered.
#3. Number of individuals who are eligible to vote but did not vote.
#4. Number of individuals who did vote.
#5. Number of records processed.

#VARIABLE DICTIONARY
#total_not_eligible_to_reg
#total_old_enough_not_reg
#total_eligible_did_not_vote
#total_voters
#total_records_processed
#id_num
#age
#registered
#voted

#this file uses: voters_202040.csv

#--IMPORTS--------------------------------------------------------------------
import csv
#--MAIN EXECUTING CODE--------------------------------------------------------

#initialize a record counting variable
total_not_eligible_to_reg = 0
total_old_enough_not_reg = 0
total_eligible_did_not_vote = 0
total_voters = 0
total_records_processed =  0

#create an empty list for every potential field in the file
id_num = []
age = []
registered = []
voted = []

#connecting to the file
with open("text_files/voters_202040.csv") as csvfile:

  file = csv.reader(csvfile)

  for rec in file:
    #parallel lists --> data dispersed across lists, connected by the same index
    id_num.append(int(rec[0]))
    age.append(int(rec[1]))
    registered.append(rec[2])
    voted.append(rec[3])


#disconnected from file

print(f"\n{"ID Number":10}  {"Age":5}  {"Registered":3}  {"Voted"}")
print("-" * 40)
for i in range(0,  len(id_num)):
    ##for every item, index will start at 0 and run up to (not including) the length (# of items)
    print(f"{id_num[i]:<10}  {age[i]:<5}  {registered[i]:10}  {voted[i]}")
print("-" * 40)

#processing lists -- USING A FOR LOOP
for i in range(0, len(id_num)):
  #calculate the number of individuals not eligible to register.
  if age[i] < 18:
    total_not_eligible_to_reg += 1
  #calculate number of individuals who are old enough to vote but have not registered.
  if age[i] >= 18 and registered[i] == "N":
    total_old_enough_not_reg += 1
  #calculate number of individuals who are eligible to vote but did not vote.
  if age[i] >= 18 and registered[i] == "Y" and voted[i] =="N":
    total_eligible_did_not_vote += 1
  #calculate number of individuals who did vote.
  if voted[i] == "Y":
    total_voters += 1
  #calculate number of records processed.
  total_records_processed += 1 

#end of program - final output displays
print(f"\nNot Eligible to Register:   {total_not_eligible_to_reg}")
print(f"Of age but not Registered:  {total_old_enough_not_reg}")
print(f"Eligible but didn't Vote:   {total_eligible_did_not_vote}")
print(f"Total number of Voters:     {total_voters}")
print(f"Total Records Processed:   {total_records_processed}")
print("\nThank you for using the program. Goodbye.\n")