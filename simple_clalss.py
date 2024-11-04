import tempfile

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



class DataBase():
    def __init__(self, name, port):
        self.name = name 
        self.port = port 

    def connect_to_db(self):
        print(f"{self.name}:///user:password:{self.port}")


alex = Person("Alex", 33)
alex.output()

web_developer = Programmer("Python", 120000)
web_developer.info()

first_book = Book("Programming on Python", 2024, "Sebastyan Rushka", "Programming")
first_book.about_book()
first_book.save_to_file("This is first a book")

mysql = DataBase("mysql", 44883)
mysql.connect_to_db()

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
