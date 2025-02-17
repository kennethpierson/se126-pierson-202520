#W3D2 - INPUT 


#Practice 1.3 continuation - making programs whose final values depend on user input


#INPUT
#the inclusion of INPUT allows a user to enter data into the program; this gives the program the opportunity to use these values in formulas and to generate unique, specific final values based on the user's needs

#THE INPUT STATEMENT
#*remember: assignment (=) occurs from RIGHT to LEFT
#      variable = value OR resulting value of process found on right side




print("\n\n\n----PRACTICE 1.3--INPUT()-------------")

#set-up: assign known values
#sometimes, the known or needed values to get started need to come from the user
totalMiles = 3158

mpg = 32

gasCost = 1.8

tollsCost = 23

lodgingCost = 360


#data relationships and manipulation 
#only NUMBERS can do math :]

#CASTING - int(), float(), and str()

totalGallons = totalMiles / mpg 

totalGasCost = totalGallons * gasCost 

totalOneWayCost = totalGasCost + tollsCost + lodgingCost

totalRoundTripCost = totalOneWayCost * 2


#test your values with print() before formatting, comment out later
print(totalOneWayCost)
print(totalRoundTripCost)

#add .format() printing to ALL FLOATS. ALWAYS
#floats are imperfect in Python 

print("\tTOTAL ONE WAY COST:     ${0:.2f} \n\tTOTAL ROUND TRIP COST: ${1:.2f}".format(totalOneWayCost, totalRoundTripCost))
#rounding printed value to 2nd decimal (not stored value)