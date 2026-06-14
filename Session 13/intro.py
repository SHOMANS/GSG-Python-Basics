user = {"name": "Hend", "age": 20, "job": "doctor"}

print(user["name"])
print(user["age"])

user["age"] += 1

print(user["age"])

# print("job" in user)
if "job" in user:
    print("user has job")

for key, value in user.items():
    print(f"her {key} is {value}")


# al_zahraa = {
#     "1": [0, 1, 2, 3],
#     "2": [0, 1, 2],
#     "3": [
#         [0, 1, {"bedroom": [0, 1], "bathroom": "", "living_room": "", "kitchen": ""}],
#         1,
#     ],
#     "4": [0, 1],
# }
