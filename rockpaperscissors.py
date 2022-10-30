disclaimer = "This game is case-sensitive, so if it says Rock, Paper or Scissors: please do not put 'rock' or 'paper' - only 'Rock' or 'Paper'. [PRESS ENTER TO CONTINUE]"
cont = input(disclaimer)
print('\n\n')
#Go Again or Finish?
goAgain = "y"
while goAgain == "y":
    import time
    #Variables
    rpsOptions =["Rock", "Paper", "Scissors"]
    userChoice = input('Rock, Paper, or Scissors? ')
    #Random Picker
    import random
    rpsIndexChoice = random.randint(0,2)
    rpsChoice = rpsOptions[rpsIndexChoice]
    #"Dialogue"
    print('Thinking...')
    time.sleep(3)
    #Outcomes
    if userChoice == "Rock":
        if rpsChoice == "Rock":
            print('It is a draw, I chose Rock!')
        if rpsChoice == "Paper":
            print('I win, Paper covers Rock!')
        if rpsChoice == "Scissors":
            print('You win, Rock blunts Scissors!')

    elif userChoice == "Paper":
        if rpsChoice == "Rock":
            print('You win, Paper covers Rock!')
        if rpsChoice == "Paper":
            print('It is a draw, I chose Paper!')
        if rpsChoice == "Scissors":
            print('I win, Scissors cuts Paper!')

    elif userChoice == "Scissors":
        if rpsChoice == "Rock":
            print('I win, Rock blunts Scissors!')
        if rpsChoice == "Paper":
            print('You win, Scissors cuts Paper!')
        if rpsChoice == "Scissors":
            print('It is a draw, I chose Scissors!')

    else:
        print('Please choose only Rock, Paper or Scissors.')

    #Ask for another game
    another = input('\nWould you like to go again? [y/n] ')
    if another == "y":
        print('\n')
        goAgain = "y"
    else:
        goAgain = "n"
        exit()
        






