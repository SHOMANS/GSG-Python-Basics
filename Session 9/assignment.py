# Ask the user to enter a number, then print its multiplication table from 1 to 10.
# number = int(input("please enter number"))
# for i in range(1, 11):
#     print(f"{i} x {number} = {number * i}")


# ------------------------------------------------------------------------
# ------------------------------------------------------------------------

# counter = 0
# for num in range(1, 31):
#     if num % 2 == 0:
#         print(num)
#         counter += 1
# print("Total even numbers found:", counter)


# ------------------------------------------------------------------------
# ------------------------------------------------------------------------


# Question 3: Password Attempts
# Write a program that asks the user to enter a password.
# The correct password is:
# "python123"
# The user has only 3 attempts.
# If the password is correct, print:
# Access granted
# If the user fails after 3 attempts, print:
# Account locked
# Hint: Use a while loop.
print("------------------------------------------------")

# correct_password = "python123"
# attamp = 0

# while attamp < 3:
#   entered_password = input('please enter an password? ')
#   if entered_password == correct_password:
#     print('access granded')
#     break
#   else:
#     print('wrong password')
#     attamp += 1

# if attamp == 3:
#   print('account blocked')

# ------------------------------------------------------------------------
# Shoman Work
# ------------------------------------------------------------------------

# correct_password = "python123"
# attempts = 3

# while attempts > 0:
#     user_password = input(f"enter your password you have {attempts} attempts ")
#     if user_password == correct_password:
#         print("access granted!")
#         break
#     else:
#         print("wrong password")
#         attempts -= 1

#     if attempts == 0:
#         print("account locked")


# ------------------------------------------------------------------------
# ------------------------------------------------------------------------


# Question 4: Calculate Average Marks
# Ask the user how many marks they want to enter.
# Then ask them to enter the marks one by one.
# Finally, print the average mark.
# Example:
# How many marks do you want to enter? 4
# Enter mark 1: 80
# Enter mark 2: 90
# Enter mark 3: 75
# Enter mark 4: 85
# Average: 82.5
# Hint: Use a loop, a total variable, and division.


# print('------------------------------------------------')

# num_marks = int(input('How many marks do you want to enter? '))
# total_marks = 0

# for i in range(num_marks):
#     mark = float(input(f'enter you mark number {i+1}? '))
#     total_marks += mark

# average = total_marks / num_marks
# print(f'your avarage is : {average}')

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------


# Question 5: Number Guessing Game
# Create a number guessing game.
# Use this fixed secret number:

# secret_number = 7
# while True:
#     guess_number = int(input('Enter your guess number:'))
#     if guess_number < secret_number:
#         print('Low')

#     if guess_number > secret_number:
#         print('Hight')

#     if guess_number == secret_number:
#         print('correct:')
#         break

# print(50 * '==')


# ------------------------------------------------------------------------
# ------------------------------------------------------------------------

# correct_number = 7

# while True:
#     number = int(input("please guess number"))
#     if number > correct_number:
#         print("too high")
#     elif number < correct_number:
#         print("too low")
#     else:
#         print("Correct")
#         break

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------


# Question 6: Simple ATM Menu
# Create a simple ATM program.
# Start with this balance:

# balance = 1000

# while True:
#     print('WELLCOME IN AL SHON BANK')
#     print('THE MENU')
#     print('1-Check the Balance:')
#     print('2-Deposit Money:')
#     print('3-Withdraw Money:')
#     print('4-Exit:')

#     value = input(' Enter Number of your opporation:')

#     if (1 == value):
#         print(f"Your Balance is {balance} USD")
#     if (2 == value):
#         deposit = float(input('how many you want to doposite: '))
#         print(f"{deposit} + {balance} = {deposit + balance}")
#         balance += deposit
#         print(f"Your Balance is {balance} USD")
#     if (3 == value):
#         withdraw = float(input('how money to want to withdraw:'))
#         print(f" {balance}-{withdraw} = {balance - withdraw}")
#         balance = balance - withdraw
#         print(f"Your Balance is {balance} USD")
#     if (4 == value):
#         print("Thank you to use our bank")
#         break


# ------------------------------------------------------------------------
# ------------------------------------------------------------------------


# Bonus 1 — Very Advanced Level: Shopping Cart System

# count = 0
# total = 0
# most = 0
# cheap = 0
# while True:
#     add = int(input("Enter item price or 0 to finish:"))
#     if add == 0:
#         break
#     elif add < 0:
#         print("enter +ve price")
#         continue
#     count += 1
#     total += add
#     # most = max(add, most)
#     if add > most:
#         most = add
#     # cheap = min(add, cheap or add)  # كيف الحركة بس
#     if add < cheap or cheap == 0:
#         cheap = add

# if count == 0:
#     print("No items were added.")
# else:
#     print(f"Number of items:{count} \n Total price:{total} \n Average item price: {total / count}\n Most expensive item:{most}\n Cheapest item:{cheap}")


# ------------------------------------------------------------------------
# ------------------------------------------------------------------------


num_students = int(input("How many students do you want to enter?"))
for s in range(num_students):
    student_name = input("enter student name: ")

    num_marks = int(input("How many marks do you want to enter? "))
    total_marks = 0

    for i in range(num_marks):
        mark = float(input(f"enter you mark number {i+1}? "))
        total_marks += mark

    average = total_marks / num_marks
    print(f"{student_name} avarage is : {average}")
