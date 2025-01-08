import random
while True:

    try:
        level = int(input("level: "))
        rand = random.randint(1 , level)
        break
    except ValueError:
        continue

while True:
    try:
        guess = int(input("Guess: "))
        if guess > rand:
            print("Too large!")
        elif guess < rand:
            print("Too small!")
        elif guess == rand:
            print("Just Right!")
            break

    except ValueError:

        continue
