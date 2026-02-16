import random

you=int(input("enter your number: "))
computer=random.choice([1, 2, 3])

print(f"you choose:{you} computer choose:{computer}")

if(computer == you):
    print("it's draw")

elif(computer==1 and you==2):
    print("you win game")

elif(computer==1 and you==3):
    print("you win game")

elif(computer==2 and you==1):
    print("you loss game")

elif(computer==2 and you==3):
    print("you win game")

elif(computer==3 and you==1):
    print("you loss game")

elif(computer==3 and you==2):
    print("you loss game")


print("Thank you, I hope you will enjoy the game")

