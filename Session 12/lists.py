# create python program,
# starts with empty list,
# then add users to the list,
# then after you finish, print the whole list


# def add_users():
#     list = []

#     while True:
#         user_input = input("please enter user (enter 0 to end): ")
#         if user_input == "0":
#             break
#         list.append(user_input)

#     return list


# def main():
#     users_list = add_users()

#     print(users_list)


# main()  # start executing from this line


# ----------------------------------------


def view_users(list):
    print(50 * "*")
    if len(list) > 0:
        print("Users List:")
        for i in range(len(list)):
            print(f"{i} - {list[i]}")
    else:
        print("users list is empty, please add users first")


def add_users(list):
    while True:
        user_input = input("please enter user (enter 0 to end): ")
        if user_input == "0":
            break
        list.append(user_input)


def update_user(list):
    view_users(list)

    updated_user_number = int(input("enter the user number you need to update: "))
    updated_user_name = input(
        f"enter new user name for ({list[updated_user_number]}): "
    )

    list[updated_user_number] = updated_user_name


def delete_users(list):
    view_users(list)
    # continue the code


def main():
    users_list = []

    print("welcome to users management system:")
    while True:
        print(50 * "=")
        print("1: for view current users list")
        print("2: for add new users")
        print("3: for updating current users")
        print("0: for exit")

        print(50 * "=")

        user_input = input("please enter the number: ")

        if user_input == "1":
            view_users(users_list)
        elif user_input == "2":
            add_users(users_list)
        elif user_input == "3":
            update_user(users_list)
        elif user_input == "0":
            break
        else:
            print("enter valid number")


main()  # start executing from this line
