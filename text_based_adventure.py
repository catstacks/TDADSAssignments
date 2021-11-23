# art import source: https://pypi.org/project/art/ 
# I installed an ascii art library project from the import source link above. 
# In Command Prompt: I used 'py -m pip --version' to ensure I had pip installed then 'py -m pip install art' to install the library. In the Python3.9(64-bit) terminal: I used 'art import *' to be able to use the library then 'tprint("game","rnd-small")' to generate the ascii used in my code below.

# The name of this text-based adventure game was created using a random name generator at https://www.fantasynamegenerators.com/video-game-names.php

def start_up_logo():
    print("  ____    __    _  _  ____  ___  _   _  ____  ____     ___  ____   ___  ____  ____  ____  ___") 
    print("'(  _ \  /__\  ( \( )(_  _)/ __)( )_( )( ___)(  _ \   / __)( ___) / __)(  _ \( ___)(_  _)/ __)'")
    print("' ) _ < /(__)\  )  (  _)(_ \__ \ ) _ (  )__)  )(_) )  \__ \ )__) ( (__  )   / )__)   )(  \__ \'")
    print("'(____/(__)(__)(_)\_)(____)(___/(_) (_)(____)(____/   (___/(____) \___)(_)\_)(____) (__) (___/'")
    print("\n")

start_up_logo()
while True:

    response = input("Do you want to play Banished Secrets? (yes/no) ")

    if response.lower().strip() == "yes":
        response = input("You are walking down a country lane during a beautiful summer's day. You see a deer in the distance to your left and a butterfly to your right. Which way will you go? (left/right) ").lower().strip()

        if response == "left":
            response == input("The deer runs further into the landscape until you are alone. Or so you think... Would you like to keep going or stay and explore the area more? (go/stay) ")
            if response == "go":
                print("you die")
            elif response == "stay":
                print("you die")    
            else:
                print("you die")
        elif response == "right":
            print("you die")
        else: print("You die instantly because you did not go left or right. That's life...")            

    else:
        print("Maybe another time then...")
        break
