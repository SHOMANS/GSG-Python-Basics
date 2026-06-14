data = [
    1,
    True,
    "Fatma",
    ["morning", "evening"],
    {
        "weather": {
            "today": "sunny",
            "tomorrow": "rainy",
            "test": ["morning", "evening"],
        }
    },
    [
        "hot",
        "cold",
        ["morning", "evening"],
        {
            "today": "sunny",
            "tomorrow": "rainy",
            "test": ["morning", "evening"],
        },
    ],
]


def format_object(tree):
    if type(tree) is list:
        for i in tree:
            format_object(i)
    elif type(tree) is dict:
        for key, value in tree.items():
            print(key)
            format_object(value)
    else:
        print(tree)


format_object(data)


# first version
# for i in data:
#     if type(i) is list:
#         for ii in i:
#             print(ii)
#     elif type(i) is dict:
#         for key, value in i.items():
#             print(key)
#             for i_key, i_value in value.items():
#                 print(i_key)
#                 print(i_value)
#     else:
#         print(i)


# morning
# evening
# weather
# today
# sunny
# tomorrow
# rainy
# hot
# cold

# print all items in this variable
# use for loop and if statement

# print(type(data) is list)
# print(type(data[1]) is dict)
