#Ken Pierson
#SE126.04
#Lab 6 Collections & Logic
#2-22-2025

#PROGRAM PROMPT: Use lists to create the airplane seating chart - either 1D or 2D lists. You may either create a file to read the data in for the seats, or you can hand-populate your own 1/2D lists. If you choose to create your own file, please upload along with your completed Lab #6 .py file. 


#variable dictionary
#rows               Empty list for the rows
#seatA              Empty list for all A seats
#seatB              Empty list for all B seats
#seatC              Empty list for all C seats
#seatD              Empty list for all D seats
#valid_row          List containing valid rows
#valid_seat         List containing valid seats
#answer             Start and stop the loop
#row_choice         Variable for user input to select a row
#seat_choice        Variable for user input to select a seat

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

def seatMap(): #function to display the seat map
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

#we will use the below hand-populated list
valid_row = ["1", "2", "3", "4", "5", "6", "7"]
valid_seat = ["A", "B", "C", "D"]

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
    row_choice = input("Enter the row you'd like to sit in [1-7]: ")    #User input to select a row
    while row_choice not in valid_row:                                  #Loop to validate user input for the row 
        print("\n***INVALID ENTRY***\n~Please try again.~\n")
        row_choice = input("Enter the row you'd like to sit in [1-7]: ")
    seat_choice = input("Enter the seat you'd like to sit in [A/B/C/D]: ").upper()     #User input to select a seat
    while seat_choice not in valid_seat:                                               #Loop to validate user input for the seat
        print("\n***INVALID ENTRY***\n~Please try again.~\n")
        seat_choice = input("Enter the seat you'd like to sit in [A/B/C/D]: ").upper()
    if row_choice == "1" and seat_choice == "A" and seatA[0] == "X":                     #Check if seat is already assiged
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")                     #Display the users row and seat choice
        print("\nThat Seat is NOT Available! Please Try Again")                          #Tell user seat is taken and to select a different seat
        seatMap()                                                                        #Display seat map
    elif row_choice == "1" and seat_choice == "A" and seatA[0] != "X":                   #Check is seat is avaiable  
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")                     #Display the users row and seat choice
        print("\nThat Seat is Available and has been assigned to you")                   #Tell user seat is avaiable and assigned to them
        seatA[0] = "X"                                                                   #Change seatA[0] to an X
        seatMap()                                                                        #Display the seat map with the seat marked as a X
    if row_choice == "2" and seat_choice == "A" and seatA[1] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "2" and seat_choice == "A" and seatA[1] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatA[1] = "X"
        seatMap()
    if row_choice == "3" and seat_choice == "A" and seatA[2] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "3" and seat_choice == "A" and seatA[2] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatA[2] = "X"
        seatMap()
    if row_choice == "4" and seat_choice == "A" and seatA[3] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "4" and seat_choice == "A" and seatA[3] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatA[3] = "X"
        seatMap()
    if row_choice == "5" and seat_choice == "A" and seatA[4] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "5" and seat_choice == "A" and seatA[4] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatA[4] = "X"
        seatMap()
    if row_choice == "6" and seat_choice == "A" and seatA[5] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "6" and seat_choice == "A" and seatA[5] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatA[5] = "X"
        seatMap()
    if row_choice == "7" and seat_choice == "A" and seatA[6] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "7" and seat_choice == "A" and seatA[6] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatA[6] = "X"
        seatMap()
    if row_choice == "1" and seat_choice == "B" and seatB[0] == "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is NOT Available! Please Try Again")
        seatMap()
    elif row_choice == "1" and seat_choice == "B" and seatB[0] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you") 
        seatB[0] = "X"
        seatMap()
    if row_choice == "2" and seat_choice == "B" and seatB[1] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "2" and seat_choice == "B" and seatB[1] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatB[1] = "X"
        seatMap()
    if row_choice == "3" and seat_choice == "B" and seatB[2] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "3" and seat_choice == "B" and seatB[2] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatB[2] = "X"
        seatMap()
    if row_choice == "4" and seat_choice == "B" and seatB[3] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "4" and seat_choice == "B" and seatB[3] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatB[3] = "X"
        seatMap()
    if row_choice == "5" and seat_choice == "B" and seatB[4] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "5" and seat_choice == "B" and seatB[4] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatB[4] = "X"
        seatMap()
    if row_choice == "6" and seat_choice == "B" and seatB[5] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "6" and seat_choice == "B" and seatB[5] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatB[5] = "X"
        seatMap()
    if row_choice == "7" and seat_choice == "B" and seatB[6] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "7" and seat_choice == "B" and seatB[6] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatB[6] = "X"
        seatMap()
    if row_choice == "1" and seat_choice == "C" and seatC[0] == "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is NOT Available! Please Try Again")
        seatMap()
    elif row_choice == "1" and seat_choice == "C" and seatC[0] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you") 
        seatC[0] = "X"
        seatMap()
    if row_choice == "2" and seat_choice == "C" and seatC[1] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "2" and seat_choice == "C" and seatC[1] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatC[1] = "X"
        seatMap()
    if row_choice == "3" and seat_choice == "C" and seatC[2] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "3" and seat_choice == "C" and seatC[2] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatC[2] = "X"
        seatMap()
    if row_choice == "4" and seat_choice == "C" and seatC[3] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "4" and seat_choice == "C" and seatC[3] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatC[3] = "X"
        seatMap()
    if row_choice == "5" and seat_choice == "C" and seatC[4] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "5" and seat_choice == "C" and seatC[4] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatC[4] = "X"
        seatMap()
    if row_choice == "6" and seat_choice == "C" and seatC[5] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "6" and seat_choice == "C" and seatC[5] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatC[5] = "X"
        seatMap()
    if row_choice == "7" and seat_choice == "C" and seatC[6] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "7" and seat_choice == "C" and seatC[6] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatC[6] = "X"
        seatMap()
    if row_choice == "1" and seat_choice == "D" and seatD[0] == "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is NOT Available! Please Try Again")
        seatMap()
    elif row_choice == "1" and seat_choice == "D" and seatD[0] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you") 
        seatD[0] = "X"
        seatMap()
    if row_choice == "2" and seat_choice == "D" and seatD[1] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "2" and seat_choice == "D" and seatD[1] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatD[1] = "X"
        seatMap()
    if row_choice == "3" and seat_choice == "D" and seatD[2] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "3" and seat_choice == "D" and seatD[2] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatD[2] = "X"
        seatMap()
    if row_choice == "4" and seat_choice == "D" and seatD[3] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "4" and seat_choice == "D" and seatD[3] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatD[3] = "X"
        seatMap()
    if row_choice == "5" and seat_choice == "D" and seatD[4] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "5" and seat_choice == "D" and seatD[4] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatD[4] = "X"
        seatMap()
    if row_choice == "6" and seat_choice == "D" and seatD[5] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "6" and seat_choice == "D" and seatD[5] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatD[5] = "X"
        seatMap()
    if row_choice == "7" and seat_choice == "D" and seatD[6] == "X":
       print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
       print("\nThat Seat is NOT Available! Please Try Again")
       seatMap()
    elif row_choice == "7" and seat_choice == "D" and seatD[6] != "X":
        print(f"\nYou choose Row: {row_choice} Seat: {seat_choice}")
        print("\nThat Seat is Available and has been assigned to you")
        seatD[6] = "X"
        seatMap()
    #Once all seats are selected will notify the user the plane is full and exit the loop and the program    
    if seatA[0] == "X" and seatA[1] == "X" and seatA[2] == "X" and seatA[3] == "X" and seatA[4] == "X" and seatA[5] == "X" and seatA[6] == "X" and seatB[0] == "X" and seatB[1] == "X" and seatB[2] == "X" and seatB[3] == "X" and seatB[4] == "X" and seatB[5] == "X" and seatB[6] == "X" and seatC[0] == "X" and seatC[1] == "X" and seatC[2] == "X" and seatC[3] == "X" and seatC[4] == "X" and seatC[5] == "X" and seatC[6] == "X" and seatD[0] == "X" and seatD[1] == "X" and seatD[2] == "X" and seatD[3] == "X" and seatD[4] == "X" and seatD[5] == "X" and seatD[6] == "X":
        answer = "n"
        print("\nThe Plane is full there are NO more available seats!")        
    else:
        answer = loopcontrol()                   #function to control the loop and only allow correct input
#Good Bye message exiting program       
print("\nThank you for using the program! Good Bye!\n")