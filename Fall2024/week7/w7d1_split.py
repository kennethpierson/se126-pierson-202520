#W7D1 - Working with the .split()

#create an error message function
def wrong():#<-- function header
    #function body - must indent!
    #contains code that will run when function is called

    print("\t***ERROR: INVALID ENTRY***")


phone = "401-789-8499"
# ip = "123.45.67.20"

phone_list = phone.split("-")

for index in range(0, len(phone_list)):
    phone_list[index] = int(phone_list[index])
    print(f"{phone_list[index]} has been cast as an integer")

rebuild_phone = ""
for index in range(0, len(phone_list)):
    if index <=2:
        rebuild_phone += str(phone_list[index]) + "."
    else:
        rebuild_phone += str(phone_list[index])
        
print(f"REBUILT STRING: {rebuild_phone}")

areaCode = int(phone_list[0])

#original string
print(phone)
#list of split string
print(phone_list)
#need the list key (index) to access specific value
print(phone_list[0])

if areaCode == 401:
    state = "RI"
    newEngland = "YES"
else: 
    state = "N/A"
    newEngland = "Maybe?"

print(f"Your phone number of {phone} has an areacode of {phone_list[0]}, which is from the state of {state} and: {newEngland} it is in New England")