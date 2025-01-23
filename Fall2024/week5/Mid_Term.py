#Name Ken Pierson
#Mid Term Project
#Date November 3, 2024
#SE116.02

#PROGRAM PROMPT: Your team will complete the Midterm Project as a group. There will be two parts to the Midterm Project. Each team will design and build a program in Python that covers the topics discussed in class from Week 1 through Week 5.

#VARIABLE DICTIONARY
#heads              holds the 1  
#tails              holds the 2
#count_wins         counting variable
#count_losses       counting variable
#total_wins         totaling variable
#total_losses       totaling variable
#choice             user Input Heads or Tails
#upperChoice        takes user input and uppercases it
#num                stores the variable for for the random number selection
#result             outcome of user choice vs random number selection
#avg_win            calculate the win loss average
#total_flips        combines the wins and losses
#wins               stores a list for a avg win percentage over 50
#random_wins        variable to select a random item out of the list
#losses             stores a list for a avg win percentage under 50
#random_losses      variable to select a random item out of the list
#tied               stores a list for a avg win percentage = to 50
#random_tied        variable to select a random item out of the list
#valid_answer       user to validate user input

#--------------------MAIN CODE--------------------

#Variables
heads = 1
tails = 2
valid_answer = False

#Counting variables
count_wins = 0
count_losses = 0
total_wins = 0
total_loses = 0

print()
print("Coin Flip! Are you ready to choose?\n")
import random
answer = "y"
while answer == "y" or answer == "Y":                          #Start of the Main Loop
    while valid_answer == False:                               #Start of a loop to ensure user input is valid (validation loop)
        choice = input("Heads or Tails?: ")
        upperChoice = choice.upper()
        if upperChoice == "HEADS":
            valid_answer = True
        elif upperChoice == "TAILS":
            valid_answer = True
        else:
            print("*** Invalid Input! Please Try Again ***")
    num = random.randint(1,2)                                   #Used to randomly select a number 
    if num == 1:
        result = "HEADS"
    else: result = "TAILS"
    if upperChoice == result:
        print(f"It's {result}! You Win!\n")
    else: print(f"It's {result}! You Lose!\n")
    if upperChoice == result:
        count_wins += 1
    if upperChoice != result:
        count_losses += 1
    answer = input("Would you like to flip again? [y/n]: ")     #exit or replay the loop
    valid_answer = False                                        #resets the prior true to send the user back through the validation loop
total_flips = count_wins + count_losses                         #calculates the total games played
avg_wins = (count_wins/total_flips) * 100                       #calculates the winning percentage
print()
print(f"You had {count_wins} win(s) and {count_losses} loss(es)! ")
print(f"Winning Percentage is: {avg_wins:.0f}%\n ")
if avg_wins > 50:                  #avg_wins greater then 50% it will look at the wins list and randomly take one entry and print it
    wins = ["Queue the victory dance!", "This victory was sponsored by sheer awesomeness.", "Try not to make winning look this easy next time.","Remember, it’s not whether you win or lose—oh who am I kidding, it totally is."]
    random_wins = random.choice(wins)       #used to select random entry for win list above
    print(random_wins)
    print()
elif avg_wins == 50:                #avg_wins equal to 50% it will look at the tied list and randomly take one entry and print it
    tied = ["So average is your legacy?", "Look, don't settle for a tie. Ain't nobody here gonna kiss their sister...I don't know why I said that", "Nobody plays for a tie...Except you I guess"]
    random_tied = random.choice(tied)       #used to select random entry for tied list above
    print(random_tied)
    print()
else:                               #when neither the if or elif above are true the else will run and a randon entry out of losses and print it 
    losses = ["Don’t worry, losing makes you stronger.", "Coin Flipping is a tough game… just kidding", "If losing builds character, you should be a superhero by now","Losing is just nature’s way of saying, you’re not there yet, but here’s a participation trophy!"]
    random_losses = random.choice(losses)   #used to select random entry for win losses list above
    print(random_losses)
    print()
print("Thanks for Flipping! And May the Odds be ever in Your Favor!\n")     #Good bye message letting the user know the code is finished