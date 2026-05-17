#Create a Python login system using nested conditions.
#The program should contain:
#A variable for the correct username
#A variable for the correct password
#A variable for the user role
#The roles can be: admin, moderator,user

# correct_name = "Jeneen"
# correct_password = "jeneen123"
# user_role = "admin"
# username = input(" enter the username: ")
# if username == correct_name:
#     password = input(" enter the password: ")
#     if password == correct_password:
#         if user_role == "Admin":
#             print("Welcome Admin")
#         elif user_role == "Moderator":
#             print("Welcome Moderator")
#         elif user_role == "User":
#             print("Welcome User")
#         else:
#             print("Unknown role")
#     else:
#         print("Wrong password")
# else:
#     print("User not found")




# ++++++++++++++++++++++++++++++++++++++++++

print("************************************")
username= input("please enter your username: ")

user1="Eid"
pass1=123
role1="Moderator"

user2="Shoman"
pass2=111
role2="Admin"

user3="Ahmed"
pass3=321
role3="User"


if username==user1 or username==user2 or username==user3:
    password= int(input("please enter your password: "))
    print("************************************\n")   
     
    # if (password == pass1 or password == pass2 or password == pass3) this is wrong

    if (username==user1 and password==pass1) or (username==user2 and password==pass2) or (username==user3 and password==pass3):
        role=input("please enter your role (Admin, Moderator, User) :")
        print("\n************************************\n")
        
        if (username==user1 and role=="Moderator")  or (username==user2 and role=="Admin") or (username==user3 and role=="User"):
            print("Welcome", role)
        
        else:
            print("Unknown role")
        
    else:
        print("Wrong password")
        
else:
    print("************************************\n")
    print("User not found")
    
print("\n************************************")





# ADMIN => admin
# "admin" == "admin" # true
# "ADMIN" == "admin" # false