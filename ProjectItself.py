import time

print('This is a test file')
name = input('What is your name? Type here: ')

if len(name) > 50:
    print("Name must contain less than 50 characters!")
    print("Name check failed - retry")
elif len(name) < 3:
    print("Name must contain 3 characters or more!")
    print("Name check failed")
else:
    print("Name looks good!")

age = input("What is your age? ")


# user input crash avoider

try:
    age_int = int(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print("Age must be a number")


def age_check(age):
    if int(age) < 18:
        print(f"{name}, you are only {age} years old! Are you sure you should be here?")
    elif int(age) > 55:
        print(f"{name} you are either lying or in the wrong place. Contact Dan.")
    else:
        print(f"You are of the appropriate age.")


age_check(age)


time.sleep(1)
print(f"\n{name}, welcome to Home Office!")
time.sleep(1)

print(f"We are happy to have you!\n")
time.sleep(1)
print("\nGet to work!")
time.sleep(1)
print('\nBut first help me with this: ')

secret_number = 2
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    try:
        guess = int(input("Try to guess my secret number! You have 5 tries. It`s between 5 and 0: "))
        guess_count += 1
        if guess == secret_number:
            print(f"Congratulations, {name}! You win!")
            break
        else:
            print(f"Nope, {name} you got it wrong. Try again!\n")
        if guess_count == guess_limit:
            print("\nSorry, you failed!")
    except ValueError:
        print("Not a valid number")
        print("Task failed successfully.")


class Human:
    def __init__(self, name):
        self.name = name

    def write(self):
        print(f"This is not {self.name}, writing.")

    def read(self):
        print(f"This is {self.name}, reading")


class Dan(Human):
    def read(self):
        print("This is Dan, a human reading this text (probably!)")


#user = Human({name})
#print(user.name)
#user.read()
print("\nThank you for using this software. You may contact me on GitHub for suggestions at username: DDSNA.")
print("\nProgram will close in 10 seconds, on its own.")
time.sleep(10)



