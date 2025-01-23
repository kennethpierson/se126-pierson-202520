



#assigning known values/gatherin needed values
temp_count = 0      #counter variable
temp_times = 5
temp_total = 0      #totaling variable

answer = "y"

while answer =="y" or answer == "Y":

#while temp_count < temp_times:
    tempF = float(input(f"Enter a temperature # {temp_count+1} in F: "))


    #date manipulation/creation of new data
    temp_count = temp_count + 1
    temp_total = temp_total + tempF
    tempC = (tempF - 32) * (5/9)

    #display solution/final results
    print(f"{tempF:.1f}F = {tempC:.1f}C")
    print(f"You have entered: {temp_count} temperatures")
    print()

    #build a way out
    answer = input("Would you like to enter another temp? [y/n]: ")

avg_temp = temp_total / temp_count
print(f"The average tempF ot {temp_count} temp is: {avg_temp:.1f}F")
print()
print(f"Thank you for using my program. \nGood Bye!\n")