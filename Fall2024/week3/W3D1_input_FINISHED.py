#W3D1 - INPUT 


#Practice 1.3 continuation - making programs whose final values depend on user input
#VARIABLE DICITONARY 
#distance     one-way distance in miles [input]
#mpg          vehicle's miles per gallon [input]
#cpg          cost per gallon of fuel, $$ [input]
#hotel_night  cost for 1 night stay in a hotel [input]
#nights       number of nights user will stay in a hotel [input]
#tolls        total cost of tolls one-way [input]

#total_gal    total gallons of gas needed for trip
#             distance / mpg
#total_hotels total hotel cost based on user's entered data  
#oneway       total cost of trip one way, $$$ 
#roundtrip    total cost of trip roundtrip, $$$


#INPUT----------------------------------------------
#the inclusion of INPUT allows a user to enter data into the program; this gives the program the opportunity to use these values in formulas and to generate unique, specific final values based on the user's needs

#THE INPUT STATEMENT
#*remember: assignment (=) occurs from RIGHT to LEFT
#      variable = value OR resulting value of process found on right side

#input("message or prompt to user")
#all input() must contain a PROMPT
#input() instruction PAUSES the code read at the line of input until it is fully executed --> the ENTER key is hit; everything before hitting ENTER is the value
#when the instruction is complete, the value REPLACES the input() statement, and next code instruction is read

#*****all data from input() is treated as a STRING

#INPUT -->  1. the program will PAUSE
#               it will not continue READING the code until the ENTER key is hit
#           2. Once ENTER is hit, the value entered will be stored to the var at left of the = and the following lines of code can be read
#           3. ALL INPUT VALUES ARE STRINGS
#               the dev must prep the program to change data types (CASTING)
#           4. BE SPECIFIC TO YOUR USER -- prompts (string messages inside of input()) need to be clear so user enters appropriate values

#utilize print() for testing -- can always comment out later
#print(distance) #displaying a stored value
#print("\n\tYou entered {} miles\n".format(distance))


print("\n\n\n----PRACTICE 1.3--INPUT()-------------")

#set-up: assign known values
#sometimes, the known or needed values to get started need to come from the user

#totalMiles = 3158
totalMiles = float(input("\n\tEnter the distance to be traveled (in miles): "))

#CASTING -- to change a value from one data type to another
#string cast --> str(VALUE)
#integer cast --> int(VALUE)
#float cast --> float(VALUE)

#YOU MUST CAST NUMERIC VALUES when gaining through input() in order to do MATH!

#ASSIGNMENT OCCURS FROM RIGHT TO LEFT; work INSIDE to OUTSIDE of PARENTHESIS

#totalMiles = float(totalMiles)

#totalMiles = float(input("Enter the distance to be traveled (in miles): "))
#mpg = 32
mpg = float(input("\n\tEnter your vehicle's MPG: "))

#gasCost = 1.8
gasCost = float(input("\n\tEnter the average cost per gallon of gas: $"))

#tollsCost = 23
tollsCost = float(input("\n\tEnter your estimated tolls for the one-way trip: $"))

#lodgingCost = 360
lodgingCost = float(input("\n\tEnter your total cost for lodging, if applicable, for the one-way trip: $"))

#data relationships and manipulation 
#only NUMBERS can do math :]

#CASTING - int(), float(), and str()

totalGallons = totalMiles / mpg 

totalGasCost = totalGallons * gasCost 

totalOneWayCost = totalGasCost + tollsCost + lodgingCost

totalRoundTripCost = totalOneWayCost * 2


#test your values with print() before formatting, comment out later
#print(totalOneWayCost)
#print(totalRoundTripCost)

#add .format() printing to ALL FLOATS. ALWAYS
#floats are imperfect in Python 

print("\tTOTAL ONE WAY COST:    ${0:.2f} \n\tTOTAL ROUND TRIP COST: ${1:.2f}".format(totalOneWayCost, totalRoundTripCost))
#rounding printed value to 2nd decimal (not stored value)