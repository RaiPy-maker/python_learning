# HILO GAME
import time
import random

# Welcome Screen

high_record = 0
currect_record = 0

print("Welcome to HiLo this is way better than Dori's version\n")

random_1 = int(random.randint(1,15))

while True:
    random_2 = int(random.randint(1,15))
    odds = random_1 / 15 * 100
    response = input(f"The number is [ {random_1} ]\nHigher (H) or lower? (L): \nOdds to win lower are {odds:.2f}% \n")



    if response == 'h' and random_1 <= random_2 or response == 'l' and random_1 >= random_2:
        print(f"Nice go next!\n")
        random_1 = random_2
        currect_record += 1
    else:
        if currect_record > high_record:
            high_record = currect_record
        print(f"You lost restart record is {high_record}\n")
        random_1 = random_2
        currect_record = 0
