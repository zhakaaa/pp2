# Take a guess
import random
random_number = random.randrange(1,20)
print(random_number)

name = input("Hello! What is your name?\n" )
print(name , "well\nI am thinking of a number between 1 and 20. Take a guess")

def take_guess(random_number) :
    count = 0
    while True :
        number = int(input())
        count+=1
        if (number == random_number) :
            answer = "Good job, {}! You guessed my number in {} guesses!"
            print(answer.format(name,count))
            break
        else :
            print("Your guess is too low. Take a guess")

take_guess(random_number)