import tempfile

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def output(self):
        print(f"{self.name} -> {self.age}")

class Sample:
    def __init__(self):
        print("Объект создан!")
        
    def __del__(self):
        print("Объект удалён!")

class Programmer(Person):
    def __init__(self, language=None, sallary=10000):
        self.language = language
        self.sallary = sallary

    def info(self):
        print( f"{self.language} -> {self.sallary}")

class Book:
    def __init__(self, title, year,author, theme):
        self.title = title
        self.year = year
        self.author = author
        self.theme = theme

    def about_book(self):
        print(f"{self.title}, {self.year}, {self.author}, {self.theme}")

    def save_to_file(self, text):
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            temp.write(b"text")
            path = temp.name
            print(path)
    
    def __del__(self):
        print("Remove object")



class DataBase():
    def __init__(self, name, port):
        self.name = name 
        self.port = port 

    def connect_to_db(self):
        print(f"{self.name}:///user:password:{self.port}")

    def info(self):
        print(f"Your database -> running")

class Postgress(DataBase):
    def about(self, base="Postgress"):
        print(f"{base}")


sample = Sample()
del sample

alex = Person("Alex", 33)
alex.output()

web_developer = Programmer("Python", 120000)
web_developer.info()

first_book = Book("Programming on Python", 2024, "Sebastyan Rushka", "Programming")
first_book.about_book()
first_book.save_to_file("This is first a book")

mysql = DataBase("mysql", 44883)
mysql.connect_to_db()


postgress = Postgress("postgress", "3323")
postgress.about()
postgress.info()

mans = (alex, web_developer)

def my_generator(my_tuple: tuple):
    for i in my_tuple:
         yield i
     

first = my_generator(mans).__iter__()
print(first)


cities = ["Moscow", "New-Yourk", "Minsk", "Minsk"]
set_cities = set(cities)
print(set_cities)

quadre = [x*2 for x in range(10)]
print(quadre)

with open("test.txt", "w") as txt:
    txt.write(""" 
                  Чтоб мудро жизнь прожить, знать надобно немало,
                  Два важных правила запомни для начала:
                  Ты лучше голодай, чем что попало есть,
                  И лучше будь один, чем вместе с кем попало.""")

with open("test.txt") as txt:
    print(txt.read())

class Vector:
    """ Class work with vectors in linear algebra"""
    def __init__(self, v1, v2):
        self.v1 = v1 
        self.v2 = v2

    def add_vectors(self):
        """Calculate vectors """
        return (self.v1[0] + self.v2[0], self.v1[1] + self.v2[1])


vectors = Vector((2, 3), (4, 5))
summa_vectors = vectors.add_vectors()
print(f"Summa of vectors = {summa_vectors}")

names_list = ["alex", "sergey", "max", "john"]
ages_list = [22, 33, 44, 27]

union_list = tuple(zip(names_list, ages_list))
print(union_list)