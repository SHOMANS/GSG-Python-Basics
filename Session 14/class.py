class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I'm {self.age} years old."

    def login(self):
        print(f"{self.name} is logged in")

    def logout(self):
        print(f"{self.name} is logged out")


user1 = User("Tasneem", 20)
user2 = User("Mahmoud", 30)
user3 = User("Ahmed", 25)


print(user1.introduce())
user1.login()
user1.logout()
