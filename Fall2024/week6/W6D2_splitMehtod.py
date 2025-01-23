#W6D2 - .split() method for Lab #5 + Building Functions & Control Flow Review
#.split() is a string method --> stringValue.split() to use
#EX: sentence = "Hello World!"; sentence.split()
#---IMPORTS-------------------------------------------------------------
#---FUNCTIONS-----------------------------------------------------------
#function definition below
def letter(numericGrade): #FUNCTION HEADER

#A function that utilizes a passed numeric grade value, finds it letter equivalent, and returns said letter equivalent

    if numericGrade >= 90:
        alphaGrade = "A"
    elif numericGrade >= 80:
        alphaGrade = "B"
    elif numericGrade >= 70:
        alphaGrade = "C"
    elif numericGrade >= 60:
        alphaGrade = "D"
    elif numericGrade >= 0:
        alphaGrade = "F"
    else: #this exists to catch any negatives or non-numeric values
        alphaGrade = "***Error in letter()***"
    return alphaGrade #this value will replace the function call in the main code
print("see you space cowboy!") #we will never see this message as it comes after the function's return
#---MAIN CODE-----------------------------------------------------------
print("W6D2 Demo\n\n")
sentence = "The quick brown fox jumps over the lazy dog!"
#display the sentence and also display the .split() version of sentence
print(f"ORIGINAL: {sentence}")
print(f" SPLIT: {sentence.split()}") #the split version isnt stored anywhere!
#print("the original was", sentence)
newSentence = sentence.split()
print(f"\n\nnewSentence: {newSentence}")
#access the first number in newSentence --> 0 is first position
print(f"\n\nthe first word is: {newSentence[0]}")
print(f"the third word is: {newSentence[2]}")
print(f"the last word is: {newSentence[len(newSentence) - 1]}")
#len() --> length --> return the count of items in a structure
print(f"There are {len(newSentence)} items in the newSentence list\n\n")
#IP ADDRESS: 110.25.13.40
#PHONE NUM3: 401-789-8499
phone = input("Enter a phone number: ")
phoneList = phone.split('-') #now splits at the - instead of space
print(phoneList)
print(f"The area code is: {phoneList[0]}")
#listName + [index] always results in 1 value with 1D lists
areaCode = phoneList[0]
print(f"The area code is: {areaCode}")
if areaCode == "401":
    print("This number is from Rhode Island!")
else:
    print("This number is NOT from Rhode Island")
#---grades and lists
classGrades = [90,88,99,64,72]
print("\n\tThe Current Class Grades")
total = 0
#for loops are built for data structures
for index in range(0, 5): #starting value of i, number of iterations
    print(f"Grade {index+1} --> {classGrades[index]}")
total += classGrades[index]
classAvg = total / len(classGrades)
print(f"The Class Average is: {classAvg:.1f}")
