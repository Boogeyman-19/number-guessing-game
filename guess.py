import random

def guess_number():
   
    a = random.randint(1, 100)
    
    attempts = 0
    max_attempts =10
    print() 
    print()
    print("\t\t\t\t***Welcome to the Number Guessing Game!***")
    print()
    print("Try guessing the number between 1 and 100.")
    print("you have only 10 guesses")
    print()

    
    while attempts < max_attempts:
        try:
            b= int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        if attempts>0:
            has_guessed=True
        if b< a:
            if has_guessed and attempts < max_attempts:
                print(b,"is lower than the random number!! Try again.")            
        elif b > a:
            if has_guessed and attempts < max_attempts:
                print(b,"is higher than the random number!! Try again.")
        else:
            print(f"Congratulations! You've guessed the number ({a}) in {attempts} attempts!")
            break
        remaining_guesses = max_attempts - attempts
        if remaining_guesses > 0:
            print("You have", remaining_guesses, "guesses remaining...\n")
    else: 
        print(f"Sorry, you've run out of attempts. The number was {a}.")


guess_number()
