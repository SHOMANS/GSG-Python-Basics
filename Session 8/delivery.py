# you have a software for a store, 
# when user order with amount less than 50 
# you will ask him to pay the amount, 
# if the order more than 50 it will be for free

# first you ask user to enter the amount of order
# check the amount if more or less than 50
# if less, you will ask him to enter "pay delivery"
# if not, just continue

# while True:
#     print(50 * "*")
#     amount = input("enter the amount you want buy or type exit to break: ")
#     if amount == "exit":
#         break
    
#     if int(amount) >= 0:
#         if int(amount) > 50:
#             print("your delivery is free!")
#             continue

#         is_payed = input("please pay the delivery fees")
#         print("it's payed")
#     else:
#         print("enter valid number")


while True:
    print(40 * "-")
    amount = int(input("please enter the amount you buy or 0 to exit: "))
    if amount >= 0:
        if amount == 0:
            exit()

        if amount >= 50:
            print("your delivery is free!")
            continue
        
        while True:
            confirmation = input("confirm delivery payment (y) ")
            if confirmation == "y":
                print("thanks for payment!")
                break
            else:
                print("you have to pay delivery")
    else:
        print("enter valid number")
