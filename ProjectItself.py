print('This is a test file')

name = input('What is your name?')


if len(name) > 50:
    print("Name must contain less than 50 characters!")
    print("Name check failed - retry")
elif len(name) < 3:
    print("Name must contain 3 characters or more!")
    print("Name check failed")
else:
    print("Name looks good!")

import time
age = input("What is your age? ")



if int(age) < 18:
    print(f"{name}, you are only {age} years old! Are you sure you should be here?")
elif int(age) > 55:
    print(f"{name} you are either lying or in the wrong place. Contact Dan.")

else:
    print(f"You are of the appropriate age.")
print("")

time.sleep(1)
print(f"{name}, welcome to Home Office!")
time.sleep(1)

print(f"We are happy to have you!")
print("")
print("Get to work!")
print('But first help me with this: ')

secret_number = 2
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    guess = int(input("Try to guess my secret number! You have 5 tries. It`s between 5 and 0"))
    guess_count += 1
    if guess == secret_number:
        print("You win!")
        break
    else:
        print(f"Nope, {name} you got it wrong. Try again!")
else:
    print("Sorry, you failed!")
