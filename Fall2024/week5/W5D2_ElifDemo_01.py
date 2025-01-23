#WEEK 5 DAY 2: If/Elif/Else Demo

#ELIF statements allow for more than two options in a program flow.  with If/Else only two differences can be included, but by adding in ELIF (else if) many options can be "chained" together.  This chaining creates a waterflow effect for how the conditions are evaluated by the processor (see demo documentation)

#PROGRAM PROMPT:
#This program simulates a grade equivalent calculator.  the user will enter a numeric grade and the program will display both the numeric as well as letter grade equivalent. This program will allow a person to enter as many grades as they want (LOOP!), and will calculate an average grade when they are finished.

#VARIABLE DICTIONARY
#total_grades       sum total of all numeric grades, needed for average
#grade_count        total number of grades entered, needed for average
#answer             value controls loop condition evaluation
#grade              numeric grade, provided by user






#---------------------------------------------------------------

print("Welcome to KT's Grade Calculator!")

#initialize necessary variables
total_grades = 0
grade_count = 0


letter_grade = "N/A"

#defining a variable --> we're storing data to it

answer = input("\nWould you like to check a grade? [y/n]: ")

#a true condition has 3 parts: 2 values, 1 comparison (relational operator)
while answer == "y" or answer == "Y":

  grade = float(input("\nEnter your numeric grade: "))
  
  grade_count = grade_count + 1
  total_grades = total_grades + grade


  #find the letter equivalent of numeric grade 
  if grade >= 90: #this is the main condition for this if/elif chain

    #if above condition is true, letter_grade value changes to "A"

    letter_grade = "A" 

  elif grade >= 80:

    letter_grade = "B"

  elif grade >= 70:

    letter_grade = "C"

  elif grade >= 60:

    letter_grade = "D"

  else:

    letter_grade = "F"


   #display to user the numeric and letter grades
  print("Your grade of {0:.2f} is a {1}".format(grade, letter_grade))


  #ask user if they have another grade (their response determines if we stay in or out of the loop)
  answer = input("Would you like to check a grade? [y/n]: ")


#calculate average
average = total_grades / grade_count

#when user quits, display their average
print("\n\n\tGRADES ENTERED: {:11}".format(grade_count))
print("        \tAVERAGE: {:10.1f}".format(average))

print("\n\n\nThank you for using my grade calculator! Now go study 8D")