from random import choice
l=["Rock","Paper","Scissors"]
def game(l):
    C_S=0
    U_S=0
    for i in range(0,3):
        n=choice(l)
        print("Choice of Computer: ", n)
        u=input("Enter your Choice: ")
        if u not in l:
            print("Invalid! Enter a valid choice")
        if n==u:
            C_S+=1
            U_S+=1
        else:
            if (n.startswith("R") and u.startswith("S")) or (n.startswith("S") and u.startswith("P")) or (n.startswith("P") and u.startswith("R")) :
                C_S+=1
            else:
                U_S+=1
            '''elif n.startswith("S") and u.startswith("R"):
                U_S+=1
            elif n.startswith("S") and u.startswith("P"):
                C_S+=1
            elif n.startswith("P") and u.startswith("R"):
                C_S+=1
            elif n.startswith("P") and u.startswith("S"):
                U_S+=1'''
    if U_S>C_S:
        print("You WON the game")
    elif U_S==C_S:
        print("It's a DRAW")
    else:
        print("Computer WON the game")
res=game(l)

