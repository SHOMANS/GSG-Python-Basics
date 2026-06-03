def capitalize_name(name):
    print(name.capitalize())
    return name.capitalize()


username = "SOJOOD"

# I have function called capitalize_name
# and it takes string value as input
# and give me capitalized string output


user_input = input("enter your username: ")


if capitalize_name(user_input) == capitalize_name(username):
    print("logged in")
else:
    print("wrong username")
