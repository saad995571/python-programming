import random
random_number = random.randint(1,100)
print("Welcome User!")

attempts = 0 
score = 100

while True:
    a= int(input("Enter Your guessed Number: "))
    attempts += 1

    if a==random_number:
       print("Congratulations!!, You guessed it right!!")
       print(f"You guessed it in{attempts} attempts. ")
       print(f"Your final score is {score}")
       break
    

    elif a < random_number:
        print("TOO LOW")
        score -= 5
        
    elif a > random_number:
        print("TOO HIGH!") 
        score -= 5

    print(f"current score: {score}")
     
