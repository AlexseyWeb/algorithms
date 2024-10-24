class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def output(self):
        print(f"{self.name} -> {self.age}")



class Programmer(Person):
    def __init__(self, language=None, sallary=10000):
        self.language = language
        self.sallary = sallary

    def info(self):
        print( f"{self.language} -> {self.sallary}")


alex = Person("Alex", 33)
alex.output()

web_developer = Programmer("Python", 120000)
web_developer.info()