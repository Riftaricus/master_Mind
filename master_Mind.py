import random

print("MasterMind")


def generate_code(length=4, digits=6):
    return [str(random.randint(1, digits)) for _ in range(length)]


def get_feedback(secret, guess):
    black_pegs = sum(s == g for s, g in zip(secret, guess))

    secret_counts = {}
    guess_counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_counts[s] = secret_counts.get(s, 0) + 1
            guess_counts[g] = guess_counts.get(g, 0) + 1

    white_pegs = sum(
        min(secret_counts.get(d, 0), guess_counts.get(d, 0))
        for d in guess_counts
    )

    return black_pegs, white_pegs


def show_secret(mystery):
    username = input("Please input a username ? ")
    password = input("Please input a password ? ")

    if login(username, password):
        code = " ".join(
            translate_to_int(int(digit)) for digit in mystery
        )
        print(code)
    else:
        print("That is not a valid account!")


def login(username, password):
    if password != "experiment":
        return False
    return username.lower() == "root"


def translate_to_color(value):
    color_to_digit = {
        "red": 1,
        "blue": 2,
        "green": 3,
        "yellow": 4,
        "purple": 5,
        "brown": 6,
    }
    return color_to_digit[value]


def translate_to_int(value):
    digit_to_color = {
        1: "red",
        2: "blue",
        3: "green",
        4: "yellow",
        5: "purple",
        6: "brown",
    }
    return digit_to_color[value]


def play_mastermind():
    print("Welcome to Mastermind!")
    print(
        "Guess the 4-digit code. Each digit is from 1 to 6. "
        "You have 10 attempts."
    )
    print("Use red, blue, green, yellow, purple or brown")

    secret_code = generate_code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        valid_guess = False

        while not valid_guess:
            guess = input(f"Attempt {attempt}: ")

            if guess.lower() == "cheat":
                show_secret(secret_code)
                continue

            input_colors = guess.split()
            if len(input_colors) != 4:
                print("Enter exactly 4 colors!")
                continue

            try:
                translated_guess = [
                    str(translate_to_color(color.lower()))
                    for color in input_colors
                ]
                valid_guess = True
            except KeyError:
                print(
                    "Invalid color. Use red, blue, green, "
                    "yellow, purple or brown"
                )

        black, white = get_feedback(secret_code, translated_guess)
        print(
            f"Black pegs (correct position): {black}, "
            f"White pegs (wrong position): {white}"
        )

        if black == 4:
            code = " ".join(
                translate_to_int(int(digit)) for digit in secret_code
            )
            print(f"Congratulations! You guessed the code: {code}")
            return

    code = " ".join(
        translate_to_int(int(digit)) for digit in secret_code
    )
    print(
        "Sorry, you've used all attempts. "
        f"The correct code was: {code}"
    )


if __name__ == "__main__":
    again = "Y"
    while again == "Y":
        play_mastermind()
        again = input("Play again (Y/n) ? ").upper()
        if again == "":
            again = "Y"
