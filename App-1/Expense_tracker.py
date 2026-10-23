budget=int(input("Enter your budget: "))
def expense_tracker(budget):
    expenses={}
    print("choice 1 - Add Expenses")
    print("choice 2 - View Expenses")
    print("choice 3 - Calculate Expenses")
    print("choice 4 - Exit")
    while True:
        choice=int(input("Enter your choice: "))
        if choice==1:
            exp_name=input("Enter expense name: ")
            exp_amount=int(input("Enter amount: "))
            expenses[exp_name]=exp_amount
        elif choice==2:
            print(f"Name  -  Amount")
            for exp_name , exp_amount in expenses.items():
                print(f"{exp_name}  -  {exp_amount} ")
        elif choice==3:
            total_amount=sum(list(expenses.values()))
            print("Total amount spent in a day: ", total_amount)
            if total_amount>budget:
                print("Your expenses exceeded your budget")
            else:
                balance_amount=budget-total_amount
                print("Balance amount is:", balance_amount)
        elif choice==4:
            break
        else:
            print("Enter a valid choice")
expense_tracker(budget)


         