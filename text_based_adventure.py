# art import source: https://pypi.org/project/art/ 
# I installed an ascii art library project from the import source link above. 
# In Command Prompt: I used 'py -m pip --version' to ensure I had pip installed then 'py -m pip install art' to install the library. In the Python3.9(64-bit) terminal: I used 'art import *' to be able to use the library then 'tprint("game","rnd-small")' to generate the ascii used in my code below.
# The name of this text-based adventure game was created using a random name generator at https://www.fantasynamegenerators.com/video-game-names.php
# Videos tutorials used as inspiration: https://www.youtube.com/watch?v=HzDcKq2NDwM&ab_channel=ElijahHenderson and https://www.youtube.com/watch?v=DEcFCn2ubSg&ab_channel=TechWithTim

import sys
import os
import random
import time

# Function for resetting console
def reset_console():
    print("\n")
    os.system('cls||clear')

def start_up(str, delay = 0.05): #Function to display start up text more slowly. Delay each letter 0.05s
    for i in str:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

def start_up_logo(): # See earliest comments
    print("  ____    __    _  _  ____  ___  _   _  ____  ____     ___  ____   ___  ____  ____  ____  ___") 
    print("'(  _ \  /__\  ( \( )(_  _)/ __)( )_( )( ___)(  _ \   / __)( ___) / __)(  _ \( ___)(_  _)/ __)'")
    print("  ) _ < /(__)\  )  (  _)(_ \__ \ ) _ (  )__)  )(_) )  \__ \ )__) ( (__  )   / )__)   )(  \__ \ ")
    print("'(____/(__)(__)(_)\_)(____)(___/(_) (_)(____)(____/   (___/(____) \___)(_)\_)(____) (__) (___/'")
    print("\n")

start_up_logo()
start_up("Banished Secrets Text Adventure Game 2021")

# Create functions for managing how text is displayed

def fprint(str, delay = 0): # When called pass in str and delay as the 2 arguments, allows for custom delays
    print("\n" + str)
    time.sleep(delay)

def sprint(str, delay = 0): # Same as the fprint but without the add newline formatting
    print(str)
    time.sleep(delay)

# Create functions for each "room" in the game
def main_hall():
    pass
def kitchen(): 
    pass
def cellar():
    pass    
def bedroom():
    pass
def secret_dungeon():
    pass
def garden():
    pass 

# Create functions with lists for tracking steps travelled
def steps():
    
    steps_made_up = []
    steps_made_down = []
    steps_made_left = []
    steps_made_right = []
    
    for i in range(1):
        steps_made_up.append(int(input("How many steps up will you walk?\n")))
    for i in range(1):
        steps_made_down.append(int(input("How many steps down will you walk?\n")))    
    for i in range(1):
        steps_made_left.append(int(input("How many steps left will you walk?\n")))
    for i in range(1):
        steps_made_right.append(int(input("How many steps right will you walk?\n")))  
    
    print(steps_made_up)
    print(steps_made_down)
    print(steps_made_left)
    print(steps_made_right)
    
    total_steps = sum(steps_made_up)+sum(steps_made_down)+sum(steps_made_left)+sum(steps_made_right)
    return total_steps


def steps_up(): 
    steps_made_up = []
    for i in range(1):
        steps_made_up.append(int(input("How many steps up will you walk?\n")))
def steps_down(): 
    steps_made_down = []
    for i in range(1):
        steps_made_down.append(int(input("How many steps down will you walk?\n")))
def steps_left(): 
    steps_made_left = []
    for i in range(1):
        steps_made_left.append(int(input("How many steps left will you walk?\n")))
def steps_right(): 
    steps_made_right = []
    for i in range(1):
        steps_made_right.append(int(input("How many steps right will you walk?\n")))

# Looped response inputs where player makes choices
while True:

    response = input("Do you want to play Banished Secrets? (yes/no) ")

    if response.lower().strip() == "yes":
        response = input("You are walking down a country lane during a beautiful summer's day. You see a deer in the distance to your left and a butterfly to your right. Which way will you go? (left/right) ").lower().strip()

        if response == "left":
            response == input("The deer runs further into the landscape until you are alone. Or so you think... Would you like to keep going or stay and explore the area more? (go/stay) ")
            if response == "go":
                steps()
            elif response == "stay":
                print("you stay")    
            else:
                print("you die")
        elif response == "right":
            print("you die")
        else: print("You die instantly because you did not go left or right. That's life...")            

    else:
        print("Maybe another time then...")
        break
