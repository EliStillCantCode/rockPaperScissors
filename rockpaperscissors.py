goAgain = True  # GAME LOOP
while goAgain:
    import time

    rpsOptions = ["Rock", "Paper", "Scissors"]  # VARIABLES
    userChoice = input('Rock, Paper, or Scissors? ')

    import random  # RANDOM PICKER
    rpsIndexChoice = random.randint(0, 2)
    rpsChoice = rpsOptions[rpsIndexChoice]

    print('Thinking...')  # DIALOGUE
    time.sleep(3)

    if userChoice.lower() == "rock":  # OUTCOMES
        if rpsChoice == "Rock":
            print('It is a draw, I chose Rock!')
        if rpsChoice == "Paper":
            print('I win, Paper covers Rock!')
        if rpsChoice == "Scissors":
            print('You win, Rock blunts Scissors!')

    elif userChoice.lower() == "paper":
        if rpsChoice == "Rock":
            print('You win, Paper covers Rock!')
        if rpsChoice == "Paper":
            print('It is a draw, I chose Paper!')
        if rpsChoice == "Scissors":
            print('I win, Scissors cuts Paper!')

    elif userChoice.lower() == "scissors":
        if rpsChoice == "Rock":
            print('I win, Rock blunts Scissors!')
        if rpsChoice == "Paper":
            print('You win, Scissors cuts Paper!')
        if rpsChoice == "Scissors":
            print('It is a draw, I chose Scissors!')

    else:
        print('Please choose from Rock, Paper or Scissors.')

    another = input('\nWould you like to go again? [y/n] ')  # PLAY AGAIN?
    if another.lower() in ['y', 'yes']:
        print('\n')
        goAgain = True
    else:
        goAgain = False
        exit()
