class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def output(self):
        print(f"{self.name} -> {self.age}")

alex = Person("Alex", 33)
alex.output()