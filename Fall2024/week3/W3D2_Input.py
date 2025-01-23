#W3D2 -- INPUT() DEMO

#INPUT --> gaining data (in this course from a user) to be used in the program itself

#PROGRAM PROMPT: This program calculates a total oneway and roundtrip cost of a cross-country drive. INPUT values have been used for flexibility within program run for user. 

#VARIABLE DICTIONARY:
#totalMiles         total distance in miles, *from user
#mpg                miles per gallon of vehicle, *from user
#tollsCost          total amount of tolls, $ *from user
#lodgingCost        total amount of hotels, $ *from user
#gasPgallon         cost of gas per gallon, $ *from user
#totalGallons       total gallons needed for drive 
#gasCost            the total cost of gas for trip, $
#oneway_cost        cost for oneway trip, $
#roundtrip_cost     cost for a rountrip, $


#------------------------------------------------------ 
#intiialize variables with known literal values to be used
#initializing a variable = defining a variable = storing an initial (starting) value 

#totalMiles = 3158

#ask user for data 'input()', store data to a var 'distance = '

totalMiles = float(input("Enter the total distance to be driven, one-way: ")) #casting input value as float()

#PYTHON SEES ALL INCOMING DATA THROUGH INPUT() AS A STRING!
#we can't do traditional math with strings:[ so we need to CAST

#mpg = 32
mpg = float(input("Enter vehicle's MPG: "))

#gasCost = 1.8
gasCost = float(input("Enter the average cost of a gallon of gas: $"))

#tollsCost = 23
tollsCost = float(input("Enter expected tolls cost: $"))

#lodgingCost = 360
lodgingCost = float(input("Enter the total expected lodging cost: $"))

totalGallons = totalMiles / mpg 

totalGasCost = totalGallons * gasCost 

totalOneWayCost = totalGasCost + tollsCost + lodgingCost

totalRoundTripCost = totalOneWayCost * 2 

print("ONE WAY TRIP COST: ${0:7.2f}\n  ROUND TRIP COST: ${1:7.2f}".format(totalOneWayCost, totalRoundTripCost))

#print("  ROUND TRIP COST: ${0:7.2f}".format(totalRoundTripCost))




