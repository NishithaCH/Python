import random
l = ["rock","paper","scissors"]
print("rock, paper or scissors?")
user = input("type your choice")
computer=random.choice(l)
print(computer)
if (computer == user):
    print("IT IS A TIE")
elif(computer=="rock" and user=="scissor"):
    print("computer won")
elif(computer=="rock" and user=="paper"):
    print("user won")
elif(computer=="scissor" and user=="rock"):
    print("user won")
elif(computer=="scissor" and user=="Paper"):
    print("computer won")
elif(computer=="paper" and user=="scissor"):
    print("user won")
elif(computer=="paper" and user=="rock"):
    print("computer won")
    
