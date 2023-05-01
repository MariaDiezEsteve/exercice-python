#Random integer function : Use a random.randint() function to get a random integer number from the inclusive range. For example, random.randint(0, 10) will return a random number from [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9, 10].

#https://pynative.com/python-random-randrange/#:~:text=Use%20a%20random.randint(),8%20%2C9%2C%2010%5D.&text=Use%20a%20random.randrange(),range%20by%20specifying%20the%20increment.

from random import randint

#Set up the variable with 3 options

choice = ["Rock", "Paper", "Scissors"]

print("Welcome to the Rock, Paper, Scissors Game:\n")

#newline character : \n (Enter a new block) - https://www.w3schools.com/c/c_newline.php#:~:text=The%20newline%20character%20(%20%5Cn%20),next%20line%20on%20the%20screen.


# COMPUTER: List to pull a random choise out so in 0 position its rock, 1 its paper, and 2 position its scissors 


computer_choice = choice[randint(0, 2)]


# USER: input to enter the choice of user. Force lower() to know if the program is working. First Capital letter for computer.

player = input("Your Choice: ").lower()

#To know the choice made of the computer

print("Computer chose: " + computer_choice)


#To print who wins with all the possibilities.

if player == computer_choice:
    print("Draw")
elif player == "rock" and computer_choice == "Paper":
    print("Player Wins")
elif player == "rock" and computer_choice == "Scissors":
    print("Player Wins")
elif player == "paper" and computer_choice == "Rock":
    print("Player Wins")
elif player == "paper" and computer_choice == "Scissors":      
    print("Computer Wins")
elif player == "scissors" and computer_choice == "Rock":
    print("Computer Wins")
elif player == "scissors" and computer_choice == "Paper":
    print("Player Wins")


#Different set up the selection process and determine who is the winner

# def main():
#     if player == computer_choice:
#         print("Draw")
#     elif player == "rock" and computer_choice == "Paper":
#         print("Player Wins")
#     elif player == "rock" and computer_choice == "Scissors":
#         print("Player Wins")
#     elif player == "paper" and computer_choice == "Rock":
#         print("Player Wins")
#     elif player == "paper" and computer_choice == "Scissors":      
#         print("Computer Wins")
#     elif player == "scissors" and computer_choice == "Rock":
#         print("Computer Wins")
#     elif player == "scissors" and computer_choice == "Paper":
#         print("Player Wins")
#     main()

# main()