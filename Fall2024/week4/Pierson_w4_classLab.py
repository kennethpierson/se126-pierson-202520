#Name Ken Pierson
#W4 # In class lab
#Date October 21, 2024
#SE116.02

#PROGRAM PROMPT: Write a robust employee wage program for an employer. This program will be similar to W3 in class lab (Lab 1 with input()), but you will also include a loop, totaling variables, and a counter variable. This program should ask an employer (the user of the program) to enter an employee’s name, hours worked in a week, and hourly wage. After this data has been input into the program, print to the user the employee’s name, gross pay for one week, taxes due for one week (use 20% or a user-entered value, up to you as long as the calculations are correct!), and this employee’s net pay. Then, allow the user to enter a new employee’s information by asking if they would like to. If the user does have another employee to enter, repeat the processes again: ask for data, run calculations, and display individual employee’s information. When the user decides they no longer have data to enter, display to them the total number of employees entered during the program session and the totals of gross pay, tax amount, and net across all employees entered. All money should be format rounded to the second decimal place and clearly labeled. All money should have decimals in alignment with one another.

#VARIABLE DICTIONARY
#employee_name
#hourly_rate        Amount made per hour  $$$
#hours_worked       Number of hours work in the Pay Period
#tax_rate           Rate of tax
#grossPay           Pre tax money  $$$
#taxes_due          Amount owed to government  $$$
#netPay             Money left  $$$
#employee_count     Number of employees
#total_gross        Total gross pay of all employees
#total_tax          Total tax of all employees
#total_net          Total net pay of all employees
#taxes 

#---------------------------------------------------------------------

#start code below :]

#Step 1: Assign Known or Gather Needed Data
print()
employee_count = 0
total_gross = 0
total_tax = 0
total_net = 0

answer = "y"

while answer == "y" or answer == "Y":
    #Step 2: Manipulate or create new data
    employee_name = str(input("Enter your First and Last Name: "))
    hourly_rate = float(input("Enter your hourly rate: $"))
    hours_worked = float(input("Enter hours worked for the Pay Period: ")) 
    grossPay = hourly_rate * hours_worked
    taxes = grossPay * 20/100
    netPay = grossPay - taxes
    employee_count = employee_count + 1
    total_gross = total_gross + grossPay
    total_tax = total_tax + taxes
    total_net = total_net + netPay

    #Step 3: Output/Display the Solution Results

    print()
    print(f"Employee:   {employee_name}")
    print(f"Gross Pay:  ${grossPay:,.2f}")
    print(f"Taxes:      ${taxes:,.2f}")
    print(f"Net Pay:    ${netPay:,.2f}")
    print()
     #build a way out
    answer = input("Would you like to enter another employee? [y/n]: ")

print(f"You have entered: {employee_count} employee(s)")
print(f"Total Gross Pay:  ${total_gross:,.2f}")
print(f"Total Taxes:      ${total_tax:,.2f}")
print(f"Total Net Pay:    ${total_net:,.2f}\n")
print("Payroll complete time for a Beer! Good Bye!\n")
