#Name Ken Pierson
#W2 # Homework lab
#Date October 9, 2024
#SE116.02

#PROGRAM PROMPT: Develop a basic Net Pay Calculator program. This will be a program that stores a user’s hourly pay (use $14.50), hours worked (32/week), and tax rate (20%), then calculates and displays the user’s gross pay,taxable amount deducted, and net pay for a two-week period. Once you have stored the available data to descriptive variables, run the appropriate calculations to find the gross pay, taxes to be deducted, and netpay – storing each into their own descriptive variables. Using these variables, display the gross pay, taxesdeducted, and net pay back to the user. Make sure the displayed data is labeled and format rounded to the second decimal place.

#VARIABLE DICTIONARY
#hourly_rate        Amount made per hour  $$$
#hours_worked       Number of hours work
#tax_rate           Rate of tax
#grossPay           Pre tax money  $$$
#taxes              Amount owed to government  $$$
#netPay             Money left  $$$

#---------------------------------------------------------------------

#start code below :]

#Step 1: Assign Known or Gather Needed Data

hourly_rate = 14.5
hours_worked = 64
tax_rate = .20

#Step 2: Manipulate or create new data

grossPay = hourly_rate * hours_worked
taxes = grossPay * tax_rate
netPay = grossPay - taxes

#Step 3: Output/Display the Solution Results

print()
print(f"Gross Pay:  ${grossPay:.2f}")
print(f"Taxes:      ${taxes:.2f}")
print(f"Net Pay:    ${netPay:.2f} ")
print()
print("Don't spend it all in one place! Good Bye!")
print()