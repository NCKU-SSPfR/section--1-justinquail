import webbrowser, sys, time, random, os  # Importing necessary modules

def input_math():
    try:
        for _ in range(3):  # Allow up to 3 attempts
            user_input = input("1 times 1 = ? ")
            if user_input == "1":
                print("Correct!")
                break
            else:
                print("Incorrect, try again!")
        else:
            raise ValueError("Too many incorrect attempts")
    except ValueError as ve:
        print(f"Caught ValueError in input_math: {ve}")

input_math()
