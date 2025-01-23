#W4D2 - While Loop Review

#Problem: Write a Python program for a student to determine their average grade for a class.  Allow the user to enter as many numeric grades as they would like. Once they are finished entering grades, display to them their average, rounded to the first decimal place, along with how many grades they entered.


# a full analysis of the program can be found in the 'W4D2 - InClassProble.pdf' in the W4D2 - Class Notes & Demo Files page, Week 4 module in Canvas

#---MAIN CODE----------------------------------

print("Welcome to My Average Grade Calculator\n")
#initialize of vars / set up for the loop

#totaling var - this will add a specific value to itself; the totaling var "grows" by a certain amount after specific actions - IF WE ARE ADDING TO IT the processor needs to know "what am i adding to?"

total_grades = 0

#counting var - this will add 1 to itself every time a specific action takes place 

count_grades = 0

#loop control variable - (key) this is the var whos value will determine the evaluation of the conditional statement (is it TRUE or FALSE) 

answer = "y"

#start loop - what needs to repeat?
#loop condition based on loop control var
while answer == "y" or answer == "Y":

#START OF LOOP!-------------------------------
  #when codition evals as TRUE, indented code runs
  
  #REPEATING -- inside of loop 1 tab indent 
  grade = float(input(f"Enter grade: {count_grades + 1}: "))
  count_grades += 1 
  total_grades += grade

  #BUILD A WAY OUT! provide the user an opportunity to change the value stored to the loop control var (answer)
  answer = input("Would you like to enter another grade? [y/n]: ")
#EXIT LOOP -- unindent back to main alignment

#calculate average of all grades 

avg_grade = total_grades / count_grades

#final display to user 
print()
print(f"With {count_grades} grades entered, your current average is a(n): {avg_grade:.1f}")

#EXTRA -- Display to the user if they are currently passing or not (assume passing is an average score of 60 or higher) -- This Extra option only needs to happen 1x! So, not a loop structure but an if statement!
if avg_grade >= 60:
    #indent in here
    print(f"Congratulations, your average of {avg_grade:.1f} means you are Passing :) \n")
else: 
    print(f"Sorry, your average of {avg_grade:.1f} means you are Failing :( \n")

print("Thank you for using my program - Goodbye!\n")
#display avg (round to 1st decimal)
#display grade count