name = "ahmed  "
print("ahmed" == name)
print("ahmed" == name.strip())
print("ahmed".upper())
print("AHMED".lower())
print(f"my name is {name}")
print(name[0])
print(name[0:3])
print(name.replace("a", "s"))

email = "my-email@gmail.com"

print("@" in email)

if "@" in email:
    print("this is valid email")
else:
    print("this is not a valid email, please retry")
