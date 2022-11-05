import random
import time
goAgain = True
while goAgain:
    userRPS = input("Rock, Paper, or Scissors? ")
    #
    if userRPS.lower() not in ['rock', 'paper', 'scissors']:
        print("\n\tOnly input ROCK, PAPER, or SCISSORS")
    else:
        #
        print("\n\tPicking...")
        time.sleep(3)
        print("\n\tFiguring out who won...\n")
        #
        time.sleep(3)
        options = ['rock', 'paper', 'scissors']
        computerRandom = random.randrange(0,2)
        computerRPS = options[computerRandom]
        #
        if userRPS.lower() == "rock":
            if computerRPS == "rock": print("We drew, I chose rock.")
            elif computerRPS == "paper": print("I win, I chose paper.")
            else: print("You win, I chose scissors.")
        #
        elif userRPS.lower() == "paper":
            if computerRPS == "rock": print("You win, I chose rock.")
            elif computerRPS == "paper": print("We drew, I chose paper.")
            else: print("I win, I chose scissors.")
        #
        elif userRPS.lower() == "scissors":
            if computerRPS == "rock": print("I win, I chose rock.")
            elif computerRPS == "paper": print("You win, I chose paper.")
            else: print("We drew, I chose scissors.")
    #
    time.sleep(3)
    anotherGame = input("\nDo you want to go again?[Y/N] ")
    if anotherGame.lower() not in ['y', 'yes']:
        print("\n\tOk, see you soon!")
        goAgain = False
    else:
        print('\n')
        goAgain = True
