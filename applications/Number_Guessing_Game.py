from random import randint
def guessing_game(n):
    for i in range(0,5):
        a=int(input("Enter your number: "))
        if n==a:
            print("Your guess is correct!")
            res=True
            break
        elif n>a:
            print("Req no is greater than your input")
            res=False
        else:
            print("Req no is smaller than your input")
            res=False
    return res
n=randint(1,10)
if guessing_game(n):
    print("You WON the game!")
else:
    print("You LOST the game")
