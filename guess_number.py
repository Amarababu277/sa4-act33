guesses_left = 3

number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

if guess == number:
    print("Congratulations! You guessed the right number.")
else:
    print(f"Sorry! The number was {number}.")
    while guesses_left > 0:
        guess = input(f"What number am I thinking of? ({guesses_left} guesses left, enter 'q' to quit) ")
    
        if guess == 'q':
            print(f"Sorry! The number was {number}.")
            break
        
        guess = int(guess)
        
        if guess == number:
            print("Congratulations! You guessed the right number.")
            break
        elif guess < number:
            print("Sorry! The number is higher. Try again.")
        else:
            print("Sorry! The number is lower. Try again.")
        
        guesses_left -= 1

    if guesses_left == 0:
        print(f"Sorry! You've run out of guesses. The number was {number}.")