# first_name = input("what is your first name? ") # input
# last_name = input("what is your last name? ") # input
# age = input("how old are you? ") # input

# result = input() 

# print("========================================")
# print(f"your name is {first_name} {last_name} your age is {age}") # output


# function:
# input()
# print()
# type()
# int()


# ================================================
# ask user to enter 2 numbers and print the sum.


first_number = input("enter the first number ") # "3" always string
# first_number = int(input("enter the first number ")) # convert to int
second_number = input("enter the second number ") # "6" always string

# "3" => string
# 3 => int


# type casting => convert type to another type
# string to integer => int("3") => 3 as integer
# string to float => float("3") => 3.0 as float
# integer to string => str(3) => "3" as string


# sum_string = first_number + second_number # string + string => concatenation
sum = int(first_number) + int(second_number) # casting to int for each input and the result is int
# sum = float(first_number) + float(second_number) # casting to float for each input and the result is float

print("==============================")
print(f"sum is {sum}")

# name = "ahmed"
# name += "kuhail"

# print(name)

# print("hello" + "ahmed") # strings with + give me concatenation

