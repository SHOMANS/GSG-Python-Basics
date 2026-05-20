current_username = "mohammed"
current_password = "123"

is_wrong_username = True
is_wrong_password = True

while is_wrong_username:
    input_username = input("Enter username: ")

    if input_username == current_username:
        is_wrong_username = False

        while is_wrong_password:
            input_password = input("Enter your Password: ")
            if input_password == current_password:
                print(f"welcome {current_username}")
                # print("welcome " + current_username)
                # print("welcome" , current_username)
                is_wrong_password = False
            else:
                print("wrong password")
    else:
        print("wrong username")
