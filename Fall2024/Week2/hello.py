#W2D1 - Basic Python Intro

#Documentation/Comments are NOT read by the computer

#Required starting documentation for Lab Files
#           *Name
#           *Lab #/Lab Title
#           *Date
#           *Program Prompt/Explaination
#           *Variable Dictionary [list of names + description]


#------------------Main Code Below----------------------------

#VARIABLES: friendly names for date within our code
#assignment of date (storage, definition) occurs using =
#once date is assigned to a variable (var) that name can be used and the processor will recognize & replace with that date

name = "Ken"        #look you can comment to the side too!
#storage occurs from RIGHT to Left
#ln 19: string value of "Ken" stored to var name 'name'

#OUTPUT: data out of the program: display of data
#output statement --> print()

#Display of Literal Message
print("Hello World!")
print() #display an empty new line in console; can also use "\n"
#display the literal string Hello World!

#Display a Stored Value
print(name)
#displays the value stored to 'name'

#Display a Mix of Stored & Literal Data - ALWAYS LABEL YOUR OUTPUT!
print(f"Hi there {name}! Welcome to SE116 :]")





tempF = 62
tempC = (tempF - 32) * (5/9)
#Always format your float values for display!
#{} hold the names of variables; after : specifies format; :.#f --> # decimal places to format round
print(f"{tempF:.2f}F is {tempC:.2f}C")
