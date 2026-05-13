'''
Create a Python program using nested if statements only.

The program should:

1. Ask the user to enter their age.
2. If the age is 18 or older:
  - Ask if the user has a ticket.
  - If the answer is "yes", print:
  "Access granted"
  - Otherwise, print:
  "You need a ticket"
3. If the age is less than 18, print:
"Access denied because of the age"

Requirements:

- Use variable
- Use nested if
- Do not use elif
- Do not use loops
'''

age = int(input("enter your age "))

if age >= 18:
    print("your age is ok")
    has_ticket = input("please write 'yes' if you have a ticket ")
    if has_ticket == "yes":
        print("Access granted")
    else:
        print("You need a ticket")
else:
    print("Access denied because of the age")
    need_change_film = input("please write 'yes' if you need to change the film")
    if need_change_film == "yes":
        print("film changed")
    else:
        print("thanks, but you can not join")


# if age >= 18 and has_ticket:
#     print("Access granted")
# else:
#     print("")