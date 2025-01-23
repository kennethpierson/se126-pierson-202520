#Name Ken Pierson
#W4 # Lab 3
#Date October 23, 2024
#SE116.02

#PROGRAM PROMPT: Write a basic cash register program that calculates a user’s total due at checkout as well as determines the change this user will receive based on this total cost of all items purchased. The user should be allowed to enter as many items as they want into the program, and they should not be expected to know how many items they have when they begin. For each item, the user should be prompted to enter the cost of the item and also be asked if the item is taxable. If the item is taxable, the program should automatically calculate the tax due for said item and display it back to the user, along with the total cost of said item (cost + tax_amount). The tax percentage is 7%. Allow the user to enter as many items as they would like. When the user has finished entering all of their items the program should display: the total number of items, the total cost of all items entered (subtotal), the total tax amount due on all taxable items (total_tax), and the final total cost (final_total + total_tax). Once the information has been displayed, prompt the user for amount tendered (how much money they will be paying with). Do not let the program continue until the user has supplied enough money! Display any change due to the user. Make sure all monetary values are displayed to the second decimal place and are clearly labeled.

#VARIABLE DICTIONARY
#item_count
#item_cost
#item_count
#item_cost
#final_total
#tax_rate
#tax_total
#sub_total
#taxed_item = item_cost * tax_rate
#item_taxed
#tax_cost

#---------------------------------------------------------------------

#start code below :]
print()
print("Welcome to the Cash register")
print()
#Step 1: Assign Known or Gather Needed Data
item_count = 0
item_cost = 0
final_total = 0
tax_rate = 0.07
tax_total = 0
sub_total = 0
taxed_item = item_cost * tax_rate
item_taxed = 0
tax_cost = 0

answer = "y"

while answer == "y" or answer == "Y":
    #Step 2: Manipulate or create new data
    item_cost = float(input(f"Enter the cost of item #{item_count + 1}: $"))
    item_count += 1
    item_taxed = str(input("Is the item taxable? [y/n]: "))
    if item_taxed == "y" or item_taxed == "Y":
        tax_cost = item_cost * tax_rate
        tax_total += tax_cost
        taxed_item = item_cost + tax_cost
        print(f"Item {item_count}: ${taxed_item:.2f}")
    else:
        print(f"Item: {item_count}: ${item_cost:.2f}")
    
    final_total += item_cost + tax_cost
    answer = input("Would you like to enter another item? [y/n]: ")

    #Step 3: Output/Display the Solution Results
print()
print("Here is your receipt:")
print()
print("----------RECEIPT----------")
print(f"Items Sold: {item_count} ")
print(f"Subtotal:   ${final_total - tax_total:.2f}")
print(f"Tax (7%):   ${tax_total:.2f}")
print(f"Total Due:  ${final_total:.2f}")
print("---------------------------")
print()


sufficent_funds = "n"
while sufficent_funds == "n" or sufficent_funds == "N":
    payment_made = float(input(f"How much will you be paying?: $"))
    if payment_made >= final_total:
        sufficent_funds = "y"
    else: 
        print("***INSUFFICENT FUNDS***")
change = payment_made - final_total
print(f"Here is your change: ${change:.2f}")

print()
print("Thank you for Shopping! Have a Nice Day!")
print()


   

