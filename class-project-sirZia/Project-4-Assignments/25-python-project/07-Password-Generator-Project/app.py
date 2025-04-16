import random
import string

print("Welcome To Your Password Generator")

# Using string module for better character definitions
chars = string.ascii_letters + string.digits + '!@#$%^&*().,^?'

while True:
    try:
        number = int(input('Amount of passwords to generate: '))
        length = int(input('Input your password length: '))
        if number <= 0 or length <= 0:
            print("Please enter positive numbers only.")
            continue
        break
    except ValueError:
        print("Please enter valid numbers only.")

print("\nHere are your Passwords:")

for pwd in range(number):
    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)