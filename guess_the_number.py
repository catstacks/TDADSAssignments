import random

# This project uses the random module in Python. 
# The program will first randomly generate a number unknown to the user. 
# The user needs to guess what that number is. (In other words, the user needs to be able to input information.) 
# If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low). 
# If the user guesses correctly, a positive indication should appear. 
# You’ll need functions to check if the user input is an actual number, to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers. Random function, Variables, Integers, Input/Output, Print, While loops, If/Else statements

def guess_game():
    number = random.randint(1, 100)
    guess = int(input('Guess a number between 1 and 100. Write your guess here: ')) 
    # Prevent invalid user inputs
    # if guess == int or 100 > guess > 1:  
    #     guess = int(input('Guess a number between 1 and 100. Write your guess here: '))   
    # else:
    #     guess = int(input('Please enter a valid integer between 1 and 100: '))    
    # Main body of game (check guess and number match)    
    if guess != number:       
        if guess > number:
            high = guess - number
            print('Sorry! Your guess is too high by', high)
        elif guess < number:
            low = number - guess
            print('Sorry! Your guess is too low by', low)
    else:
        print("Gadzooks! You've guessed the number correctly!")
# Loop to give user option to play again        
    guess_again = str(input('Would you like to guess again? Please enter Y or N to continue: '))
    while guess_again == 'Y':
        return guess_game()
    print('Thanks for playing!') 
    
guess_game()        




        
