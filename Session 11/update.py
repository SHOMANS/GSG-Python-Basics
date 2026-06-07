# names_list = ["Ahmed", "Amjad", "Eid", "Feda", "Mahmoud", "Nour", "Soha"]
# names_list = ["Ahmed", "Amjad", "Eid Oukal", "Feda", "Mahmoud", "Nour", "Soha"]
# print("before", names_list)
# names_list[2] = "Eid Oukal"
# print("after", names_list)


# name = "Eid"
# print(name)

# name = "Eid oukal"
# print(name)


# you have names_list
# names_list = ["Ahmed", "Amjad", "Eid", "Feda", "Mahmoud", "Nour", "Soha"]
# create function that concat the surname to the first name for each name
# for every name, you will ask the user to give you the surname for the current item
# then you print the updated array

names_list = ["Ahmed", "Amjad", "Eid", "Hend"]
print("before function", names_list)


def add_surnames(list):
    for i in range(len(list)):
        print("name before change", list[i])
        surname = input(f"enter the surname for {list[i]}: ")
        list[i] = list[i] + " " + surname
        print("name after change", list[i])


add_surnames(names_list)
print("after function", names_list)  # list item values changed

# def add_surnames(list):
#     for i in range(len(list)):
#         surname = input(f"enter the surname for {list[i]}: ")
#         list[i] += (
#             " " + surname
#         )  # when update the list item, it update the original values
#     list = (
#         []
#     )  # when re assign value to the list itself, it doesn't change the original value
#     return list


# name = "ahmed"


# def add_singe_surname(name):
#     name += " surname"
#     print("inside function", name)


# add_singe_surname(name)
# print("outside function", name)  # original variable value didn't change
