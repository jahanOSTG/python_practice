from random import randint

# Ask for user input
guessNumber = int(input("Enter your guess (between 1 and 5): "))

# Generate a random number between 1 and 5
randomNumber = randint(1, 5)

# Check if the guessed number matches the random number
if guessNumber == randomNumber:
    print("You Win! The number was", randomNumber)
else:
    print("You Lose! The number was", randomNumber)
