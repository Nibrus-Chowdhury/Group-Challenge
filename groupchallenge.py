"""
Nibrus Chowdhury, Grace Cao, Cesar
10/21/24
Period 5-6
Description: User guesses a random number from 1 to 10, or 1 to 50, or 1 to 1000 and the computer responds if that is high or low until the user gets the answer 
"""
import random
import time

# Declaring the variables
rounds = int(input("How many rounds do you want to play?"))
total_rounds = rounds
difficulty = input("How difficult do you want it? (1-10, 1-50, 1-1000)")
ran_num1 = random.randint(1,10)
ran_num2 = random.randint(1,50)
ran_num3 = random.randint(1,1000)
attempts = 0
attempts_total = 0
#function to play the game
def attempt(attempts, rounds, difficulty, ran_num1, ran_num2, ran_num3, total_rounds, attempts_total):
    if difficulty == "1-10": 
        random_num = ran_num1 
    elif difficulty == "1-50":
        random_num = ran_num2
    else: 
        random_num = ran_num3
    #starts timer
    time1 = time.time()
    user_guess = int(input("What is your guess?"))
    if user_guess == random_num:
        print(f"It took you: {attempts} attempts to guess the number")
        attempts_total = attempts_total + attempts
        attempts = 0
        rounds -= 1
        #ends timer and gives response
        time2 = time.time()
        print('Response time: {:0.2f} seconds'.format(time2-time1))
        if rounds > 0:
            print("\nNew Round")
            attempt(attempts, rounds, difficulty, ran_num1, ran_num2, ran_num3, total_rounds, attempts_total)
        else:
            print("End of game!")
            print(attempts_total/total_rounds,"average number of attempts per round")
    else:
        attempts += 1
        #ends timer and gives response
        time2 = time.time()
        print('Response time: {:0.2f} seconds'.format(time2-time1))
        if user_guess > random_num:
            print("Too high")
            attempt(attempts, rounds, difficulty, ran_num1, ran_num2, ran_num3, total_rounds, attempts_total)
        else:
            print("Too low")
            attempt(attempts, rounds, difficulty, ran_num1, ran_num2, ran_num3, total_rounds, attempts_total)
attempt(attempts, rounds, difficulty, ran_num1, ran_num2, ran_num3, total_rounds, attempts_total)
