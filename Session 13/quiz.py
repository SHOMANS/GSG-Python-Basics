# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# *+++++++++++++++++++++++++++++ Live Quiz +++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ! Dataset 1

data = [
    ["apple", "banana", ["cat", "dog"]],
    {"name": "Ali", "age": 20, "city": "Gaza"},
    ["red", "blue", "green"],
]


# * 1. Print `"banana"`
# print(data[0][1])
# * 2. Print `"dog"`
# print(data[0][2][1])
# * 3. Print `"Ali"`
# print(data[1]["name"])
# * 4. Print `20`
# print(data[1]["age"])
# * 5. Print `"green"`
# print(data[2][2])

# ?++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ! Dataset 2

data = {
    "student": {"name": "Sara", "grades": [80, 90, 100]},
    "colors": ["red", "yellow", "black"],
    "active": True,
}


# * 6. Print `"Sara"`
# print(data["student"]["name"])
# * 7. Print `90`
# print(data["student"]["grades"][1])
# * 8. Print `100`
# print(data["student"]["grades"][2])
# * 9. Print `"yellow"`
# print(data["colors"][1])
# * 10. Print `True`
# print(data["active"])

# ?++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ! Dataset 3

data = [
    {"name": "Omar", "skills": ["Python", "HTML", "CSS"]},
    {"name": "Lina", "skills": ["JavaScript", "React"]},
]


# * 11. Print `"Omar"`
# print(data[0]["name"])
# print(data[0]["name"][0]) # will print O (first index in Omar)
# * 12. Print `"CSS"`
# print(data[0]["skills"][2])
# * 13. Print `"Lina"`
# print(data[1]["name"])
# * 14. Print `"React"`
# print(data[1]["skills"][1])

# ?++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ! Dataset 4

data = {
    "shop": [
        {"name": "Book Store", "items": ["pen", "book", "notebook"]},
        {"name": "Tech Store", "items": ["mouse", "keyboard", "screen"]},
    ]
}


# * 15. Print `"Book Store"`
# print(data["shop"][0]["name"])
# * 16. Print `"notebook"`
# print(data["shop"][0]["items"][2])
# * 17. Print `"Tech Store"`
# print(data["shop"][1]["name"])
# * 18. Print `"keyboard"`
# print(data["shop"][1]["items"][1])
# * 19. Print `"screen"`
# print(data["shop"][1]["items"][2])

# ?++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ! Dataset 5

data = [
    {"country": "South Africa", "cities": ["Cape Town", "Johannesburg"]},
    {"country": "Palestine", "cities": ["Gaza", "Ramallah"]},
]


# * 20. Print `"South Africa"`
print(data[0]["country"])
# * 21. Print `"Cape Town"`
print(data[0]["cities"][0])
# * 22. Print `"Palestine"`
print(data[1]["country"])
# * 23. Print `"Ramallah"`
print(data[1]["cities"][1])

# ?++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ! Dataset 6

data = {
    "user": {
        "username": "mohammed",
        "contact": {"email": "test@email.com", "phone": "123456"},
    },
    "numbers": [5, 10, 15],
}


# * 24. Print `"mohammed"`
print(data["user"]["username"])
# * 25. Print `"test@email.com"`
print(data["user"]["contact"]["email"])
# * 26. Print `"123456"`
print(data["user"]["contact"]["phone"])
# * 27. Print `15`
print(data["numbers"][2])

# ?++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ! Dataset 7

data = [
    ["morning", "evening"],
    {"weather": {"today": "sunny", "tomorrow": "rainy"}},
    ["hot", "cold"],
]


# * 28. Print `"evening"`
print(data[0][1])
# * 29. Print `"sunny"`
print(data[1]["weather"]["today"])
# * 30. Print `"rainy"`
print(data[1]["weather"]["tomorrow"])
# * 31. Print `"cold"`
print(data[2][1])
