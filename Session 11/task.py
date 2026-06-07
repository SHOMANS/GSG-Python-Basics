names_list = ["Ahmed", "Amjad", "Eid", "Feda", "Mahmoud", "Nour", "Soha"]
names_list2 = ["Feda", "Mahmoud", "Nour", "Soha"]
names_list3 = ["Ahmed", "Amjad", "Nour", "Soha"]
# create a function takes the names_list as input
# and print hello Ahmed and hello amjad and so on for each item


def great_name(list):
    for i in list:
        print(f"Hello {i}")


great_name(names_list)
great_name(names_list2)
great_name(names_list3)
