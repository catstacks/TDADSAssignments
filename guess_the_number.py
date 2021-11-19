import random

number = random.randint(1, 100) # this must be outside function so that the randomly generated number is the same if someone tries again. Credit: Folarin Olagbuyiro

def guess_game():
    
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




        
