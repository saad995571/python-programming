import random
random_number=random.randint(1,100)
while True:
    b=int(input("Guess the number:"))
    if b==random_number:
        print("Jacpot!")
        break
    elif b<random_number:
        print("You are low")
    elif b>random_number:
        print("You are high")
