import random

options = ['rock', 'paper', 'scissors']

while True:
    user = input("\nrock, paper, scissors? (or 'quit'): ").lower()
    if user == 'quit': break
    if user not in options:
        print("Invalid choice! Try again.")
        continue
    
    computer = random.choice(options)
    print(f"Computer chose: {computer}")
    
    if user == computer:
        print("Tie!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")