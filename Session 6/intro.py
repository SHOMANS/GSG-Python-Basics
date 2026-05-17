correct_username = "Lenovo"
correct_password = "123"

# while expression: => it will enter the loop only if the expression is True
is_retry_username = True
is_retry_password = True

while is_retry_username:
    username = input("enter username: ")

    if username == correct_username:
        password = input("enter your password: ")
        is_retry_username = True
        while is_retry_password:

            if correct_password == password:
                print("you are authorized")
                is_retry_password = False

    else:
        print("username or password is incorrect")
        print("try again")


# while True:
#     print("this is infinity loop")


print("loop is done")


# you have variables for correct username and password.
# you will ask the user to enter username.
# then check if username is correct continue.
# if not, repeat the process again to let the user re-enter the username.
# then if username is true, ask him to enter password.
# and repeat the process until the password is correct then end the program.