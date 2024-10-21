"""
Nibrus Chowdhury
10/21/24
Period 5-6
Description: User guesses a random number from 1 to 10 and the computer responds if that is high or low until the user gets the answer 
"""
import random
import time

rounds = int(input("How many rounds do you want to play?"))
difficulty = input("How difficult do you want it? (1-10, 1-50, 1-1000)")
ran_num1 = random.randint(1,10)
ran_num2 = random.randint(1,50)
ran_num3 = random.randint(1,1000)
attempts = 0


def attempt(ran_num, attempts, rounds):
    if difficulty == "1-10": 
        random_num = ran_num1 
    elif difficulty == "1-50":
        random_num = ran_num2
    else: 
        random_num = ran_num3
    if rounds > 0:
        user_guess = int(input("What is your guess? 1-10"))
        time1 = time.time()
        if user_guess == ran_num:
            print(f"It took you: {attempts} attempts to guess the number")
            rounds -= 1
            time2 = time.time()
            print('Response time: ', time2 - time1)
        else:
            attempts += 1
            print('Response time: ', time2 - time1)
            if user_guess > ran_num:
                print("Too high")
                attempt(ran_num, attempts)
            else:
                print("Too low")
                attempt(ran_num, attempts)
    else:
        print("End of game!")
attempt(ran_num, attempts)
