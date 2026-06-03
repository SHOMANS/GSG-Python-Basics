# function without input or output
# function with input but without output
# function without input but with output
# function with input and output
import random


# function without input or output (void)
def hello():  # no parameter
    print("hello!")  # no return


# function with input but without output (void)
def hello_name(name):  # with parameter
    print(f"hello {name}!")  # no return


# function without input but with output
def random_number():  # no parameter
    print("inside", random.randrange(1, 10))  # with return


# function with input and output
def calculate_sum(first_number, second_number):  # with parameter
    return first_number + second_number  # with return


# hello()
# hello_name("Mahmoud")

my_random_number = random_number()
print(my_random_number)
# calculate_sum()
