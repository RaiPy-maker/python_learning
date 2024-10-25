# Random guessing game
import random

lowest_int = 1
highest_int = 100

rand = random.randint(lowest_int, highest_int)
print(rand)
print("You have 5 Guesses!\n")
guesses = 5
while True:
    for i in  range(guesses):
        guessed_num = int(input("Guess the number: "))

        if guessed_num > rand:
            print("Too high try again!")
        elif guessed_num < rand:
            print("Too low try again!")
        elif guessed_num == rand:
            print(f"Correct the number was {rand}")
            break
    break
