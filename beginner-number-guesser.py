import random

top_of_range = input("Type a number")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0 :
        print("Please type a number greater than 0")
        quit()
else:
    print("Please type a number")
    quit()


random_number = random.randint(0,top_of_range)
guess = 0
while True:
    if guess >= 5:
        print("You are out of guesses")
        break
    user_guess = input("Make a guess: ")
    if(user_guess.isdigit()):
        user_guess = int(user_guess)
    else:
        print("Please enter a number")
        continue
    if user_guess == random_number:
        print("Correct !!!!")
        break
    else:
        print(str(5 - guess)+' guesses left')
        guess += 1
        continue    
