'''Q11. Create a class Printer with a method print() that works with:
1 string
2 strings
multiple strings (simulate overloading)'''

class Printer:
    def print(self, *args):
        if len(args) == 0:
            print("Nothing to print.")
        elif len(args) == 1:
            print("Printing one string:", args[0])
        elif len(args) == 2:
            print("Printing two strings:", args[0], "and", args[1])
        else:
            print("Printing multiple strings:")
            for i, item in enumerate(args, start=1):         #enumerate(iterable, start=0)
                print(f"{i}: {item}")

# Example usage
p = Printer()

p.print()                         # 0 args
p.print("Hello")                  # 1 string
p.print("Hello", "World")         # 2 strings
p.print("One", "Two", "Three")    # Multiple strings
