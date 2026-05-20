# write a program in python to print all numbers between 0 and 10 
# but if the current value is 5, don't continue

# for item in range(11):
#     print(item)
#     if item == 5:  
#         break


# take input from user, and it should be int
# print all numbers from 0 to 10 after multiply them by the input number
# if anytime the result is 9 end the loop, and stop

user_input = int(input("enter the number: "))

for number in range(11):
    result = number * user_input
    if result == 9: break # it won't print 9, it will break the loop directly
    print(result)

for number in range(11):
    result = number * user_input
    print(result)
    if result == 9: break 