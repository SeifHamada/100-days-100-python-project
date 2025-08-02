import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculate():
    num1 = int(input("Enter your first number: "))
    while True:
        for i in operators:
            print(i)
        symbol = input("Enter your symbol: ")
        num2 = int(input("Enter your second number: "))
        answer = operators[symbol](num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            print("\n" * 100)
            calculate()
            break


calculate()