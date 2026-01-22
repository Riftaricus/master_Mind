#!/bin/python3
# MasterMind
# by ICTROCN
# v1.01
# 15-8-2024
# Last mod by Morris
print("MasterMind")

import random

def generate_Code(length=4, digits=6):
    return [str(random.randint(1, digits)) for _ in range(length)]

def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))
    
    # Count whites by subtracting black and calculating min digit frequency match
    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)
    
    return black_Pegs, white_Pegs

def show_Secret(mystery):
    username = input("Please input a username ? ")
    password = input("Please input a password ? ")

    if isAdmin := login(username, password):
        code = " ".join([translateToInt(int(digit)) for digit in mystery])
        print(code)
    else:
        print("That is not a valid account!")
        return
    
def login(username, password):
    return False if password != "experiment" else username.lower() == "root"
    
def translateToColor(input):
    color_to_digit ={
        "red": 1,
        "blue": 2,
        "green": 3,
        "yellow": 4,
        "purple": 5,
        "brown": 6,
    }
    return color_to_digit[input]
def translateToInt(input):
    digit_to_color ={
        1: "red",
        2: "blue",
        3: "green",
        4: "yellow",
        5: "purple",
        6: "brown",
    }
    return digit_to_color[input]
    

def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-digit code. Each digit is from 1 to 6. You have 10 attempts.")
    print("Use red, blue, green, yellow, purple or brown")
    secret_Code = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = ""
    
        
        valid_Guess = False
        
        while not valid_Guess:
            guess = input(f"Attempt {attempt}: ")
            if guess.lower() == "cheat":
                show_Secret(secret_Code)
                continue
            
            inputColors = guess.split()
            if len(inputColors) != 4:
                print("Enter exactly 4 colors!")
                continue
            try:
                translated_guess = [str(translateToColor(color.lower())) for color in inputColors]
                valid_Guess = True
            except KeyError:
                print("Invalid color. Use red, blue, green, yellow, purple or brown")
            
            

        black, white = get_Feedback(secret_Code, translated_guess)

        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            code = " ".join([translateToInt(int(digit)) for digit in secret_Code])
            print(f"Congratulations! You guessed the code: {code}")

            return
    code = " ".join([translateToInt(int(digit)) for digit in secret_Code])
    print(f"Sorry, you've used all attempts. The correct code was: {''.join(code)}")

if __name__ == "__main__":
    again = 'Y'
    while again == 'Y':
        play_Mastermind()
        again = input("Play again (Y/n) ? ").upper()
        if again == "":
            again = "Y"
