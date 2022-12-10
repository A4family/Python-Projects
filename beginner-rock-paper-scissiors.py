import random
user_wins = 0
computer_wins = 0
game_sets = ['r','p','s']
while True:
    user_input = input("Type r for rock, p for papper and s for scissors or q to quit the game").lower()
    if user_input == "q":
        break
    
    if user_input not in game_sets:
        print("Please type r for rock, p for papper and s for scissors or q to quit the game")
        continue 

    computer_input = game_sets[random.randint(0,2)]
    print("Computer picked "+ str(computer_input))
    # rock is 0 , papper is 2 and scissors is 2
    if user_input == 'r' and computer_input == 'p':
        computer_wins += 1
        print("Computer wins try again !! Computer wins: "+str(computer_wins)+ " Your wins : " + str(user_wins))
    elif user_input == 'p' and computer_input =='s':
        computer_wins += 1
        print("Computer wins try again !! Computer wins: "+str(computer_wins)+ " Your wins : " + str(user_wins))
    elif user_input == 's' and computer_input == 'r':
        computer_wins += 1
        print("Computer wins try again !! Computer wins: "+str(computer_wins)+ " Your wins : " + str(user_wins))
    else:
        user_wins += 1
        print("You win!! Computer wins: "+str(computer_wins)+ " Your wins : " + str(user_wins))

print("Good Bye !!!!")