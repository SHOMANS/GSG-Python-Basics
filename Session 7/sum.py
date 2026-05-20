#  write a program in python to calculate the sum of the range between 2 numbers
#  you ask the user to enter the first number then the second number.
#  you calculate the sum of all numbers between and include them.


first_number = int(input("please enter the first number: ")) # 1
second_number = int(input("please enter the second number: ")) # 10

# sum = 0
# sum +=  first_number  # 1
# sum += first_number + 1 # 2 => 3
# sum += first_number + 2 # 3 => 6
# sum += first_number + 3 # 4 => 10

counter = first_number  # 1
sum = 0

while counter <= second_number:
    print(f"{sum} + {counter} = {sum + counter} => sum = prev_sum + current_counter_value")
    sum += counter
    # sum = sum + counter 
    counter += 1

print(50 * "=")
print(f"sum of number between {first_number} and {second_number} is : {sum}")