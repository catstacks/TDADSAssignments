import random
def dice_roll():
    sides = int(input('Input the number of sides on your die: '))
    roll = random.randint(1, sides)
    print('You rolled a', roll)   
    roll_again = str(input('Would you like to roll again? Please enter Y or N to continue: '))
    if roll_again == 'Y':
        return dice_roll()
    else: 
        print('Thanks for playing!') 
  
dice_roll()
    

