# for i in range(1, 11):
#     if i == 5 or i == 7 or i == 2:
#         continue
#     print(i)

# even number
# print all even numbers between 8 and 37, but use continue instead
# for number in range(8, 38):
#     if number % 2 != 0:
#         continue
#     print(number)

# you have list of items, and if user choose "milk" it will be for free
free_item = "milk"

while True:
    print("please choose item from this list (coffee, milk, late)")
    print(f"{free_item} is for free!!")
    print("if you finished please enter 0")
    item = input("choose item ")

    print(f"you selected {item}")
    if item == "0":
        print("Good bye :'(")
        # exit() # terminate the whole session, close the program
        break  # only break the current loop, the program will continue working 

    if item == free_item:
        print("your drink is for free!! enjoy!")
        continue
    print(50 * "=")
    print("please pay the amount: ")
    input("enter the amount you will pay ")
    print("thank you for the payment :)")
    print(50 * "=")
    print(50 * "=")

print("the store is closed")
