import random

#1. We want to ask to a user to guess the number. If the user guesses the number: 

top_of_range = input("Type a number: ") #this input give us a string and we need a number. we ask to the user use a number as a stop the range. 

#1.1 Check if the number is integer:
        #We need to know if user enter a integer number between 0 and the number stop in our range:

if top_of_range.isdigit(): #isdigit(): Check if all the characters in the text are digits. Give us true or false.
    top_of_range = int(top_of_range)  #int change from string to number. 
    
    if top_of_range < 0:
        print("Please type a number larger than 0 next time.")
        quit() #Scape to the console. 
else:  
        print("Please type a number next time.") #If it is not a number show me this message
        quit() #Scape to the console. 

#2. you can use to make random numbers: https://www.w3schools.com/python/module_random.asp
        #print(random.randrange(start, stop)): the numbre stop is not include
        #print(random.randrange(stop)): if you want to start in 0 you don't need include
        #number_random = random.randrange(21)
        #number_random = random.randint(0, 21) include 21 in the number random. Use a random.randint() function to get a random integer number from the inclusive range. For example, random.randint(0, 10) will return a random number from [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9, 10].

number_random = random.randint(0, top_of_range) #We put on the stop the number which users introducce in the input
#print(number_random)
guesses = 0 #To keep how many times the user guess the number.Thes score is equal to 0

while True:
        guesses += 1
        user_guess = input("Make a guess: ") #We ask to user to guess the number
        if user_guess.isdigit():#Check if user_guess is a number is the same like we make to know if top_of_range is a number
                user_guess = int(user_guess) #If it is not a number, we convert to a number 
        else:
                print('Please type a number next time.')
                continue
        if user_guess == number_random:
                print("You got it!")
                break
        elif user_guess > number_random: #To check if the number is above o below the user_guess number
                print("You were above the number")
        else:
                print("You were below the number")

#3.We want to keep track of how many times the user actually makes a guess.
print("You got it in", guesses, "guesses")