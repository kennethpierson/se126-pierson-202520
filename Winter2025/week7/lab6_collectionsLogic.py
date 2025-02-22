#Ken Pierson
#SE126.04
#Lab 6 Collections & Logic
#2-22-2025

#PROGRAM PROMPT: Use lists to create the airplane seating chart - either 1D or 2D lists. You may either create a file to read the data in for the seats, or you can hand-populate your own 1/2D lists. If you choose to create your own file, please upload along with your completed Lab #6 .py file. 


#variable dictionary

#--IMPORTS---------------------------------------------
import csv
#--FUNCITONS-------------------------------------------
def loopcontrol(): #() is empty so NO parameters; this function does not require any info to run
  ans = input("Would you like to reserve another seat? [y/n]: ").lower()
  #check the ans value, repeat back to user if necessary
  while ans != "y" and ans != "n":
    print("***INVALID ENTRY***")
    ans = input("Would you like to reserve another seat? [y/n]: ").lower()
  #return the ans value tp be used in the base program!
  return ans

def seatMap():
    print(f"{'ROW':3}   {'A':3} {'B':3}   {'C':3} {'D':3}")
    print("---------------------------------------------------------------")
    for i in range(len(seatA)):
        print(f"{i + 1:3}   {seatA[i]:3} {seatB[i]:3}   {seatC[i]:3} {seatD[i]:3}")
    print("---------------------------------------------------------------")

#--MAIN EXECUTING CODE---------------------------------
#create lists

all_seats = [
    ['1','A','B','C','D'],
    ['2','A','B','C','D'],
    ['3','A','B','C','D'],
    ['4','A','B','C','D'],
    ['5','A','B','C','D'],
    ['6','A','B','C','D'],
    ['7','A','B','C','D'],
    ]

for i in range(len(all_seats)):
    for x in range(len(all_seats[i])):
        print(all_seats[i][x], end='')
    print()
    
    
'''

seatA = ['A', 'A', 'A', 'A', 'A', 'A', 'A']
seatB = ['B', 'B', 'B', 'B', 'B', 'B', 'B']
seatC = ['C', 'C', 'C', 'C', 'C', 'C', 'C']
seatD = ['D', 'D', 'D', 'D', 'D', 'D', 'D']

row = int(input("Enter which row you'd like to sit in [1-7]: "))
seat = input("Enter which seat you'd like to sit in [A/B/C/D]: ")


answer = "y"

while answer == "y":
  
  answer = loopcontrol()
'''