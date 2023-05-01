#We want to ask the usser a bunch of questions and if the give us the rigth answer to these question, we will kind of add one to their score. 

print("Welcome to the Quiz Game")

#Ask to the users if the want to play the game

#Input: write in the console
playing = input("Do you want to play? ")

#print(playing) - Give back the answer write for a user

#Whai it's going to happen when the user say yes or no

if playing.lower() != "yes":
    print("Back again, when you feel ready")
    quit() #quit() function is another in-built function, which is used to exit a python program.
    
print("Okay, Let's play!")

#.lower() to made the text intruducting for the user to lower case.

#We want to know how many correct answer get the user.
score = 0

answer = input("1. How do I print 'Hello, World' to the console in Python? ")

if answer  == 'print("Hello, World")':
    print('Correct!')
    score += 1
else:
    print('Incorrect, you need to use a print() and inside you need to write the sentence there is in the question. Solution: print("Hello, World")')
    
answer = input("2. How do I declare a variable in Python? Declares a variable x with a value of 5. Introduce an space between the declaration. ")

if answer.lower() == 'x = 5':
    print('Correct!')
    score += 1
else:
    print("Incorrect, to declare a variable in Python, you simply assign a value to a variable name using the equals sign (=). Solution: x = 5")

answer = input("3. Python code is written in plain text files with a _______ extension")

if answer.lower() == '.py':
    print('Correct!')
    score += 1
else:
    print("Incorrect, You use it to create a file in VSC to know is python file. Solution: .py")

answer = input("4. Comments begin with the ____________ character and continue to the end of the line. They are ignored by the Python interpreter.")

if answer == '#':
    print('Correct!')
    score += 1
else:
    print("Incorrect, you use a # to create a comment. Solution: #")

#str(): to keep the score in a string variable. We can't add a number: score with an string. That we need str()

print("You got " + str(score) + " questions correct!")

#to get the rate of the answers correct

print("You got " + str((score / 4) * 100) + " %")