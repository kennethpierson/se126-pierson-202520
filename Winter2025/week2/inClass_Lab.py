#Ken Pierson
#SE126.04
#W2D2 In Class Lab
#1-16-2025 [W2D2]

#PROGRAM PROMPT: The csv file classLab2.csv contains a list of rooms, the maximum number of people that the room can accommodate, and the number of people currently registered for the event. Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit


#VARIABLE DICTIONARY:
#total_rooms        initializes the variable
#rooms_over         initializes the variable
#file               variable for the csv file
#room_name          variable for the rooms in the csv
#cap_max            variable for the max capacity of the room
#num_ppl            variable for the number of people in the room
#over_under         variable for calculating max capacity minus number of people

#--IMPORTS---------------------------------------------
import csv

#--FUNCITONS-------------------------------------------
#this function returns the difference between the 2 values it's passed people and max_cap
def difference(people, max_cap):
    diff = max_cap - people 
    return diff

#--MAIN EXECUTING CODE---------------------------------

#initialize the counting variables
total_rooms = 0
rooms_over = 0 

print(f"{'ROOM NAME':20}     {'MAX':5}   {'PPL':5}   {'OVER'}")
print("---------------------------------------------")

#-----connected to file--------
with open("text_files/classLab2.csv") as csvfile:
    
    file = csv.reader(csvfile)

    #for loop: This loop structure iterates through each line in the file, assigning the content of the line to the record variable.
    #record: This is a variable that will hold the contents of each line in the file as the loop iterates.
    #file: This represents the file object that you've opened for reading.
    for record in file:
    
        #assign variable names
        room_name = record[0]
        cap_max = int(record[1])
        num_ppl = int(record[2])

        #calls the function
        over_under = difference(num_ppl, cap_max)

        #calulates the data in the file
        if over_under < 0 : 
            rooms_over += 1
            print(f"{room_name:20}   {cap_max:5}   {num_ppl:5}   {over_under * -1:5}")

        #counting variable
        total_rooms += 1

#-----Final Output--------
print(f"\nThere are {rooms_over} rooms currently OVER CAPACITY")
print(f"There were a total of {total_rooms} checked")
print("\nThank you for using the program. Goodbye.\n")