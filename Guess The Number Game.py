import random
random_number = (random.randint(0, 20))  # Uses "random" to choose a number between 0 and 20.
print(random_number)

raw_input_number = input("Choose a number between 1 and 20: ")
input_number = int(raw_input_number)
chosen_number = input_number  # Saves the user's input.


if random_number == chosen_number:
    print("Well done!")  # Tells the user that they have the right answer.

elif random_number > chosen_number:
    print("Too low!")

elif random_number < chosen_number:
    print("Too high!")

while random_number != chosen_number:
    raw_input_number = input("Choose a number between 1 and 20: ")
    input_number = int(raw_input_number)
    chosen_number = input_number  # Saves the user's input.

    if random_number == chosen_number:
        print("Well done!")  # Tells the user that they have the right answer.
        break  # This links the "while" loop and ends the programme.

    elif random_number > chosen_number:  # This tells the user that their guess is too low!
        print("Too low!")
        continue  # This links the "while" loop and continues the programme.

    elif random_number < chosen_number:  # This tells the user that their guess is too high!
        print("Too high!")
        continue  # This links the "while" loop and continues the programme.
