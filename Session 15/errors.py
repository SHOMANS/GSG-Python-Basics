while True:
    try:
        age = int(input("please enter your age: "))
        print(age)
        print(type(age))
        break

    except ValueError:
        print("invalid input, please try again")


print("after input")


# try:
#     with open("file.txt", "r") as f:
#         print(f.read())

# except FileNotFoundError:  # you must define the error type
#     print("file not exist")


# print("after error")
