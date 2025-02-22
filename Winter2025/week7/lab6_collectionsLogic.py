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
    print(f"\n{'ROW':3}   {'A':3} {'B':3}   {'C':3} {'D':3}")
    print("-" * 50)
    for i in range(len(rows)):
        print(f"{i + 1:3}   {seatA[i]:3} {seatB[i]:3}   {seatC[i]:3} {seatD[i]}")
    print("-" * 50)

#--MAIN EXECUTING CODE---------------------------------
#create an empty list for every potential field in the file
rows = []
seatA = []
seatB = []
seatC = []
seatD = []

#connecting to the file----------------------------------
with open("text_files/seats.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #parallel lists --> data dispersed across lists, connected by the same index
        rows.append(rec[0])
        seatA.append(rec[1])
        seatB.append(rec[2])
        seatC.append(rec[3])
        seatD.append(rec[4])

#disconnect from file-----------------------------------
seatMap()
answer = "y"
while answer == "y":
    row_search = input("Enter the row you'd like to sit in [1-7]: ")
    seat_choice = input("Enter the seat you'd like to sit in [A/B/C/D]: ").upper()
    if row_search == "1" and seat_choice == "A":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatA[0] = "X"
        seatMap()
    elif row_search == "2" and seat_choice == "A":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatA[1] = "X"
        seatMap()
    elif row_search == "3" and seat_choice == "A":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatA[2] = "X"
        seatMap()
    elif row_search == "4" and seat_choice == "A":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatA[3] = "X"
        seatMap()
    elif row_search == "5" and seat_choice == "A":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatA[4] = "X"
        seatMap()
    elif row_search == "6" and seat_choice == "A":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatA[5] = "X"
        seatMap()
    elif row_search == "7" and seat_choice == "A":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatA[6] = "X"
        seatMap()
    if row_search == "1" and seat_choice == "B":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatB[0] = "X"
        seatMap()
    elif row_search == "2" and seat_choice == "B":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatB[1] = "X"
        seatMap()
    elif row_search == "3" and seat_choice == "B":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatB[2] = "X"
        seatMap()
    elif row_search == "4" and seat_choice == "B":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatB[3] = "X"
        seatMap()
    elif row_search == "5" and seat_choice == "B":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatB[4] = "X"
        seatMap()
    elif row_search == "6" and seat_choice == "B":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatB[5] = "X"
        seatMap()
    elif row_search == "7" and seat_choice == "B":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatB[6] = "X"
        seatMap()
    if row_search == "1" and seat_choice == "C":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatC[0] = "X"
        seatMap()
    elif row_search == "2" and seat_choice == "C":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatC[1] = "X"
        seatMap()
    elif row_search == "3" and seat_choice == "C":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatC[2] = "X"
        seatMap()
    elif row_search == "4" and seat_choice == "C":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatC[3] = "X"
        seatMap()
    elif row_search == "5" and seat_choice == "C":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatC[4] = "X"
        seatMap()
    elif row_search == "6" and seat_choice == "C":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatC[5] = "X"
        seatMap()
    elif row_search == "7" and seat_choice == "C":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatC[6] = "X"
        seatMap()
    if row_search == "1" and seat_choice == "D":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatD[0] = "X"
        seatMap()
    elif row_search == "2" and seat_choice == "D":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatD[1] = "X"
        seatMap()
    elif row_search == "3" and seat_choice == "D":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatD[2] = "X"
        seatMap()
    elif row_search == "4" and seat_choice == "D":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatD[3] = "X"
        seatMap()
    elif row_search == "5" and seat_choice == "D":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatD[4] = "X"
        seatMap()
    elif row_search == "6" and seat_choice == "D":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatD[5] = "X"
        seatMap()
    elif row_search == "7" and seat_choice == "D":
        print(f"\nYou choose row {row_search} seat {seat_choice}")
        seatD[6] = "X"
        seatMap()
            
    answer = loopcontrol()
print("Thanks for using the program! Good Bye!")