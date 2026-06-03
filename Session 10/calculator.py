def calculator():
    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    def multiplication(a, b):
        return a * b

    def division(a, b):
        return a / b

    print("Welcome to Calculator")
    while True:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        operation = input("Enter the operation(+,-,*,/): 0 to exit ")

        if operation == "0":
            break
        elif operation == "+":
            print(addition(first_number, second_number))
        elif operation == "-":
            print(subtraction(first_number, second_number))
        elif operation == "*":
            print(multiplication(first_number, second_number))
        elif operation == "/":
            print(division(first_number, second_number))
        else:
            print("invalid operation, please try again!")


def bank_system():
    balance = 1000

    def deposit():
        deposit_value = float(input("how many you want to deposit: "))
        print(f"{deposit_value} + {balance} = {deposit_value + balance}")
        balance += deposit_value
        print(f"Your Balance is {balance} USD")

    def withdraw():
        withdraw_value = float(input("how money to want to withdraw:"))
        print(f" {balance}-{withdraw_value} = {balance - withdraw_value}")
        balance = balance - withdraw_value
        print(f"Your Balance is {balance} USD")

    while True:
        print("WELCOME IN AL MY BANK")
        print("THE MENU")
        print("1-Check the Balance:")
        print("2-Deposit Money:")
        print("3-Withdraw Money:")
        print("4-Exit:")

        value = input(" Enter Number of your operation:")

        if "1" == value:
            print(f"Your Balance is {balance} USD")
        if "2" == value:
            deposit()
        if "3" == value:
            withdraw()
        if "4" == value:
            print("Thank you to use our bank")
            break


def main_menu():
    print("welcome to the program")
    while True:
        print("1: for calculator")
        print("2: for guessing game")
        print("3: for bank management system")
        print("0: for exit")
        user_input = input("enter your input: ")

        if user_input == "1":
            calculator()
        elif user_input == "3":
            bank_system()

        if user_input == "0":
            print("thank you for your visit!")
            print("have a great time, good bye :)")
            exit()


main_menu()
