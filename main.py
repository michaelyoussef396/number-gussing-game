import random

flag = True
while flag:
    num = input("Type a number for a upper bound: ")

    if num.isdigit():
        print("Let's Play")
        num = int(num)
        flag = False
    else:
        print("Invalid input. Please type a number")

secret = random.randint(1, num)

guess = None
count = 1

while guess != secret:
    guess = (input("please type a number between 1 and " + str(num) + ": "))
    if guess.isdigit():
        guess = int(guess)
    if guess == secret:
        print("You got it!")
    else:
        print("Please try again")
        count += 1

print("It took you" + str(count) + "guesses!")
