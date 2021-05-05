import random 
import math

randomNum = random.randint(1,9)

# print(randomNum)

guesses = 0

guessNumber = int(input("Guess A Number Between 1-9: "))

while guesses < 4 :
    if(guessNumber != randomNum):
        print("Wrong Try Again!")
        guesses = guesses + 1
        guessNumber = int(input("Guess A Number Between 1-9: "))
        if(guesses == 4):
            print("Game Over You Lose!")
    elif(guessNumber == randomNum):
        guesses = 6
        print("Correct, Congrats!")


    