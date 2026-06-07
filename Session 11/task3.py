# create a function that take the empty list
# create empty list variable inside the function
# ask the user to give the length of the list
# create loop to store the items one by one inside the list,
# then print all list items
# run the function 3 times, one with numbers, then with names,
# then with products


def create_list():
    list = []
    length = int(input("enter the list length: "))
    type = input("enter the list items type: ")
    for i in range(length):
        entered_item = input(f"enter item number {i} :")
        if type == "int":
            entered_item = int(entered_item)
        list.append(entered_item)

    return list


print(create_list())
print(create_list())
print(create_list())
