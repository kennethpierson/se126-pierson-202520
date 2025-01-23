#Name Ken Pierson
#W2D2 - Practice 1.3 Full Solution Build
#Date October 9, 2024
#SE116.02

#PROGRAM PROMPT: Problem: Katie wants to drive cross-country, from Providence, RI to San Francisco, CA.  Assume this route will take 3158 miles and reserve $23.00 for tolls one-way.  Base your gas needs on the current average of $1.80/gallon.  The vehicle Corey will be driving gets an average of 32mpg and has a tank capacity of 12 gallons.  Corey will be the only driver, so with a travel time of 42 hours he will need to stop at 3 different locations to sleep (assume they do not add time, distance, or gas) and each night's rest and stay will cost $120.  No other humans or animals are accompanying him on this trip, and he will have packed all of his food beforehand.  He is not towing anything heavy, and you may assume normal travel conditions for both roadways and weather. Corey would like to know how much it would cost to get him from Providence to San Francisco.  Calculate both the total cost for this trip as a one-way and as a roundtrip expedition.


#REQUIRED STARTING DOCUMENTATION

#VARIABLE DICTIONARY
#distance           The total distance to travel one-way
#mgp                The MPG of the vehicle
#tolls              The one-way cost of tolls $$$
#nights             Number of nights staying in hotel
#hotels             Hotel nightly cost $$$
#gasPgallon         Average price per gallon of gas $$$
#totalGallons       Total gallons of gass needed for the one-way trip
#gasCost            Total gas cost for one-way trip $$$
#oneway_cost        Total cost of the trip oneway
#roundtrip_cost     Total cost of the trip there and back

#--MAIN CODE-------------------------------------------------------

#Step 1: Assign Known or Gather Needed Data
distance = 3158
mpg = 32
tolls = 23
gasPgallon = 1.8
nights = 3
hotels = 120 * nights


#Step 2: Manipulate or create new data
totalGallons = distance / mpg
gasCost = totalGallons * gasPgallon

oneway_cost = gasCost + hotels + tolls
roundtrip_cost = oneway_cost * 2


#Step 3: Output/Display the Solution Results

print(f"\tOne Way Cost:    ${oneway_cost:.2f}")
print(f"\tRound Trip Cost: ${roundtrip_cost:.2f}")