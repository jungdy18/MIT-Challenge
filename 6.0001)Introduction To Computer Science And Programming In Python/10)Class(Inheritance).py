class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def set_name(self,name):
        self.name = name
    def __str__(self):
        return "Name : " + str(self.name) + "and Age : " + str(self.age)

class Person(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.set_name(name)
        self.friends = []
    def get_name(self):
        return str(self.friends)
    def add_friends(self, friend_name):
        if friend_name not in self.friends:
            self.friends.append(friend_name)
    def age_diff(self,other):
        return str(abs(self.age - other.age))
    def __str__(self):
        return "Person " + str(self.name) + "'s age is " + str(self.age) + "." + "\nAnd his name friends are " + str(self.friends)


