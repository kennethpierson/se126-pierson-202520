#Name Ken Pierson
#W3 # In class lab
#Date October 14, 2024
#SE116.02

#PROGRAM PROMPT: This is the same as Lab 1 except instead of using assignment statements for hours worked, hourly rate, and number of weeks for a pay period, use the input statement to assign values to variables. Ask the user to input their hourly rate and their hours worked in a week, as well as the number of weeks for this pay period. You may still use 20% for the tax rate or ask the user for their tax rate as a whole number percentage (including this additional input statement, if calculations and final values are correct, will award you +5 bonus points on this in-class lab!). Once you have this information, you want to display the user’s Gross Pay, Taxes deducted, and the User’s Net Pay. All calculations should be limited to run once, rather than numerous times. Include in your flowchart the use of variables and both output as well as input statements

#VARIABLE DICTIONARY
#hourly_rate        Amount made per hour  $$$
#hours_worked       Number of hours work in the Pay Period
#tax_rate           Rate of tax
#grossPay           Pre tax money  $$$
#taxes              Amount owed to government  $$$
#netPay             Money left  $$$

#---------------------------------------------------------------------

#start code below :]

#Step 1: Assign Known or Gather Needed Data
print()
hourly_rate = float(input("Enter your hourly rate: $"))
hours_worked = float(input("Enter hours worked for the Pay Period: "))
tax_rate = float(input("Enter tax rate - Example 20% enter 20: " ))

#Step 2: Manipulate or create new data

grossPay = hourly_rate * hours_worked
taxes = grossPay * tax_rate/100
netPay = grossPay - taxes

#Step 3: Output/Display the Solution Results

print()
print(f"Gross Pay:  ${grossPay:,.2f}")
print(f"Taxes:      ${taxes:,.2f}")
print(f"Net Pay:    ${netPay:,.2f}")
print()
print("Don't spend it all in one place! Good Bye!\n")