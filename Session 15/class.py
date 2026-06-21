class User:
    def __init__(self, name, age):
        self.__name = name  # private: not accessible from outside
        self.age = age

    def introduce(self):
        return f"My name is {self.__name} and I'm {self.age} years old."

    def login(self):
        print(f"{self.__name} is logged in")

    def logout(self):
        print(f"{self.__name} is logged out")

    def get_name(self):  # getter: to get value from outside
        return self.__name

    def set_name(self, name):  # setter: to set an object attribute with new value
        self.__name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


user1 = User("Tasneem", 20)
user2 = User("Mahmoud", 30)
user3 = User("Ahmed", 25)

# print(user1.get_name())  # Tasneem
# user1.set_name("ahmed")
# print(user1.get_name())  # ahmed

print(user1.__name)
