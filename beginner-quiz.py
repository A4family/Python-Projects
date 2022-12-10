print("Welcome to my quiz game")
playing  = input("Do you want to play ?")
if playing.lower() != "yes":
    quit()
print("Okay")
score = 0
answer = input("What does cpu stand for?")
if answer != "central processing unit":
    print("Incorrect you got"+str(score))
    quit()
else:
    print("Correct !! onto the next one")
    score += 1

answer = input("What is 1 + 1 ?")
if answer == '2':
    print("correct")
    score += 1
else:
    print("Incorrect you got "+str(score))
    quit()

