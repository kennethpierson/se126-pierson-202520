#W9D1 - Course Review

#PROGRAM PROMPT: Write a program that allows the user to enter a person's ﬁrst name, last name, hourly rate, hours worked, and number of dependents. The program should display the person’s full name using one variable, gross pay, net pay and amount of money that is deducted from their pay based on the number of dependents. The user should be allowed to enter as many employees as they want. Once the user has ﬁnished entering the data the program should display the total number of employees entered, total gross pay, total net pay and total amount of deductions.





#---IMPORTS---------------------------------------------------
from os import system, name
#---FUNCTIONS-------------------------------------------------
def clear():
  '''This function has 0 params and 0 returns; its job is to clear the screen whenever it is called''' #This big string will show in pop-ups!

  if name == "nt": #for windows
    _ = system("cls")
  else: #for mac or linux
    _ = system("clear")

def loopcontrol(): #() is empty so NO parameters; this function does not require any info to run

  ans = input("Would you like to enter more data? [y/n]: ").lower()

  #check the ans value, repeat back to user if necessary
  while ans != "y" and ans != "n":
    print("***INVALID ENTRY***")
    ans = input("Would you like to enter more data? [y/n]: ").lower()

  #return the ans value tp be used in the base program!
  return ans
  print("See ")



#"A function must be used to ﬁnd each user’s deduction amount – def deduction_func(gp, dep)"
def deduction_func(gp, dep):
  print("deduction_func() called")
  #a.	The function should be sent the user’s gross pay (gp) and number of dependents (dep)
  #b.	The function should determine the gross pay reduction percentage based on the number of dependents
  if dep == 0:
    remove = 0.1  #10% --> 10/100
  elif dep == 1:
    remove = 0.08
  elif dep == 2:
    remove = 0.06
  elif dep >= 3:
    remove = 0.03
  else:
    print("***ISSUE IN deduction_func()")
    return 0
  #c.	The function should calculate the total amount value of deductions

  deduct = gp * remove
  #d.	The function should return the value of deductions to the base program

  return deduct
  #e.	You must write a unit test for this function and submit a screenshot of the passed test as a part of your lab submission


#---MAIN CODE-------------------------------------------------
clear()
print("Welcome to the Wage Calculator!\n")
#set up for main program loop - initialize known and gather needed data 
total_employees = 0
total_gross = 0
total_taxes = 0
total_net = 0 

#EXTRA: storing data to parallel lists
employees = []
emp_gross = []
emp_taxes = []
emp_net = []

answer = input("Would you like to start the Wage Calculator? [y/n]: ").lower()

#invalid entry trap - user will only enter this if they do not follow the directions from prior prompt
while answer != "y" and answer != "n":
  print("***INVALID ENTRY***")
  answer = input("Would you like to start the Wage Calculator? [y/n]: ").lower()

#"When checking to see if the user wants to enter more data they should be able to enter a y or a Y. (lowercase or uppercase)""
#main program loop - repeats for each employee
while answer =="y":

  first = input("Enter Employee's First Name: ")
  last = input("Enter Employee's Last Name: ")

  #string concatenation
  full = first + " " + last

  rate = float(input("Enter Employee's Hourly Rate: $"))
  hours = float(input("Enter Employee's Hours worked for this pay period: "))
  #tax = float(input("Enter Employee's Tax Rate [5% -> 5]: "))
  dependents = int(input("Enter # of Employee's Dependents:"))

  #indiv employee calculations
  gross = rate * hours
  #tax_amount = gross *(tax/100)
  #tax/100 gives decimal value of whole %
  tax_amount = deduction_func(gross, dependents)
  net = gross - tax_amount

  #update running counts and totals for end of program
  total_employees = total_employees + 1
  total_gross += gross
  total_taxes += tax_amount
  total_net += net

  #for EACH employee: "the program should display the person's full name (ﬁrst and last), gross pay, net pay, and amount of deductions all on one line"
  print(f"{full}: Gross ${gross:.2f} | Taxes ${tax_amount:.2f} | Net ${net:.2f}")

  #BUILD A WAY OUT OF THE LOOP!
  #"When checking to see if the user wants to enter more data they should be able to enter a y or a Y. (lowercase or uppercase)""
  answer = loopcontrol()
  '''answer = input("\nDo you have another employee to enter? [y/n]: ").lower()
    while answer != "y" and answer != "n":
    print("***INVALID ENTRY***")
    answer = input("Do you have another employee to enter? [y/n]: ").lower()'''

  clear()

#end of program - final output displays
#"Once the user is ﬁnished entering employees the program should display the number of employees, total gross pay, total net pay and total deductions"
print("\n\nThank you for that information, here is the final display:\n ")
print(f"  TOTAL EMPLOYEES: {total_employees:7}")
print(f"      TOTAL GROSS: ${total_gross:10,.2f}")
print(f" TOTAL TAXES PAID: ${total_taxes:10,.2f}")
print(f"        TOTAL NET: ${total_net:10,.2f}")

#EXTRA - ask user if they'd like to see the parallel list data 
listData = input("\nBefore exiting, would you like to review the employee data? [y/n]: ").lower()

if listData == "y":

  #show data from all lists - use a for loop! 
  for i in range(0, len(employees)):
    print(f"show list data in here :]")


print("\n\nThank you for using my program. Goodbye :]")