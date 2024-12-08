from functools import singledispatch
from random import shuffle
import re
import decimal

# 1. converting an Integer into Decimals
integer = 100
print(decimal.Decimal(integer))
print(type(decimal.Decimal(integer)))

# 2. converting an String of Integer into Decimals
str_numbers = '123456789'
print(decimal.Decimal(str_numbers))
print(type(decimal.Decimal(str_numbers)))

# 3. Reversing a String using an Extended Slicing Technique
string = 'Noobs of Python'
print(string[::-1])

# 4. Counting Vowels in a give word
vowel = ['a', 'e', 'i', 'o', 'u']
word = 'programming'
count = 0
for character in word:
    if character in vowel:
        count += 1
print(count)

# 5. Counting Consonants in a given word
count = 0
for character in word:
    if character not in vowel:
        count += 1
print(count)

# 6. Counting the number of occurances of a character in a String
word = "Javascript"
character = 'a'
count = 0
for i in word:
    if i == character:
        count += 1
print(count)

# 7. Writing Fibonacci Series
fib = [0, 1]
n = 5
for i in range(n):
    fib.append(fib[-1] + fib[-2])
print(', '.join(str(e) for e in fib))

# 8. Finding the maximum numbers in a list
numberList = [12, 3, 55, 23, 6, 78, 33, 4]
max = numberList[0]
for num in numberList:
    if max < num:
        max = num
print(max)

# 9. Finding the minimum numbers in a List
min = numberList[0]
for num in numberList:
    if min > num:
        min = num
print(min)

# 10. Finding the middle Element in a list
midElement = int(len(numberList) / 2)
print(numberList[midElement])

# 11. Converting a list into a string
list = ['p', 'y', 't', 'h', 'o', 'n']
string = "".join(list)
print(string, type(string))

# 12. Adding Two list elements together
list1 = [1, 2, 3]
list2 = [4, 5, 6]
res_list = []
for i in range(0, len(list1)):
    res_list.append(list1[i] + list2[i])
print(res_list)

# 13. Comparing two strings for anagrams
str1 = "Python programmist  "
str2 = "Python programmist"
str1 = str1.replace(" ", "").upper()
str2 = str2.replace(" ", "").upper()

if sorted(str1) == sorted(str2):
    print("True")
else:
    print("False")

# 14. Checking for palindrome using extended slicing technique
str1 = "Kayak".lower()
if str1 == str1[::-1]:
    print("Palindrome ", str1)
else:
    print("False")

# 15. Counting the white spaces in a string
string = "P r ogram in g"
print(string.count(" "))

# 16. Counting Digits, Letters and Spaces in a String
name = 'Python is 1'
digitCount = re.sub("[^0-9]", "", name)
letterCount = re.sub("[^a-zA-Z]", "", name)
spaceCount = re.findall("[ \s]", name)
print(len(digitCount), len(letterCount), len(spaceCount))

# 17. Counting Special Characters in a string


def count_sp_char(string):
    sp_char = "!@#$%^&*()<>?/\[]{};~`"
    count = 0
    for i in string:
        if i in sp_char:
            count += 1
    return count


text = "Hello! How are you? #specialchars! 123"
result = count_sp_char(text)
print(result)

# 18. Removing all whitespace in a String
string = "C O D E"
spaces = re.compile(r'\s+')
result = re.sub(spaces, "", string)
print(result)

# 19. Building a Pyramid in Python


def pyramid(n):
    for i in range(n):
        for j in range(i, n):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        for j in range(i):
            print("*", end="")
        print("")


pyramid(8)

# 20. Randomizing the items of a List in Python
lst = ['Python', 'is', 'Easy']
shuffle(lst)
print(lst)

# 21. Create a generator to produce first n prime numbers


def isprime(num):
    for i in range(2, num):
        if num % 1 == 0:
            return False
    return True


def prime_generator(n):
    num = 2
    while n:
        if isprime(num):
            yield num
            n -= 1
        num += 1


# 22. Implementing variable length arguments in python
def average(*t):
    avg = sum(t) / len(t)
    return avg


result = average(32, 5, 65, 22, 87, 34, 2, 57)
print("Average is: ", result)

# 23. Creating instance member variables in python


class Test:
    def __init__(self):
        self.a = 5

    def f1(self):
        self.b = 10


t1 = Test()
t2 = Test()
t1.c = 15
print(t1.__dict__)
print(t2.__dict__)

# 24. Addition using Lambda functions
print((lambda a, b: a+b)(3, 4))

# 25. Finding factorial using lambda function


def f(n): return 1 if n == 0 else n*f(n-1)


print(f(5))

# 26. List Compression
l1 = [2*e for e in range(1, 10)]
print(l1)

# 27. What is the use of split and join function of str
s = "What is right in your mind is right in your world"
sl1 = s.split(" ")
print(sl1)
s1 = sl1[::-1]
print(s1)
print(" ".join(s1))

# 28. Global and local variable
x = 5


def f1():
    global x
    x = 15  # global variable update
    y = 10  # local variable
    print("x=%d y=%d" % (x, y))


f1()
print(x)

# 29. Globals function
x = 5


def fun():
    x = 10  # local variable
    d = globals()  # d is dictionary
    print('local x=%d globa x=%d' % (x, d['x']))


fun()

# 30. Type conversion basics
x = int('123')
a = float('123.42')
b = complex('3+4j')
c = str(12)
d = bool('True')
e = bin(25)
f = oct(24)
g = hex(25)
h = ord('A')
i = chr(98)
print(x, a, b, c, d, e, f, g, h, i)

# 31. Type conversion
x = 5
print(type(x))
s1 = '123'
print(type(s1))
print(str(x) + s1)
print(x + int(s1))

# 32. Decorator


def welcome(fx):
    def mfx(*t, **d):
        print("Before hello function")
        fx(*t, **d)
        print("Thanks for using the function")
    return mfx


@welcome
def hello():
    print("Hello ! ")


@welcome
def add(a, b):
    print(a+b)


hello()
add(1, 3)

# class decorator


class Calculator:
    def __init__(self, func):
        self.function = func

    def __call__(self, *t, **d):
        result = self.function(*t, **d)
        return result ** 2


@Calculator
def add(a, b):
    return a + b


print(add(10, 32))

# 33. Iterators and Generators
l1 = [23, 65, 22, 76, 34, 98, 43]
it = iter(l1)
while True:
    try:
        print(next(it))
    except StopIteration:
        break


def evenNum(n):
    i = 1
    while n:
        yield 2*i
        i += 1
        n -= 1


it = evenNum(10)
evenList = []
while True:
    try:
        evenList.append(next(it))
    except StopIteration:
        break
print(evenList)

# 34. Function overloading allowed in python?
# Using default arguments


def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"


print(greet("Alexsey"))
print(greet("Alexsey", "Hi"))

# Using Variable-Length arguments


def add(*t):
    return sum(t)


print(add(1, 30))
print(add(1, 2, 3))

# Using functools.singledispatch


@singledispatch
def process(value):
    raise NotImplementedError("Unsupported type")


@process.register(int)
def _(value):
    return f"Processing an integer: {value}"


@process.register(str)
def _(value):
    return f"Processing a string: {value}"


print(process(10))
print(process("Hello"))

# Using Class Methods


class Math:
    @staticmethod
    def multiply(a, b):
        return a*b

    @staticmethod
    def multiply(a, b, c):
        return a*b*c


class Math:
    @staticmethod
    def multiply(*t):
        result = 1
        for num in t:
            result *= num
        return result


print(Math.multiply(2, 3))
print(Math.multiply(2, 3, 4, 5))

# 35. Postitional arguments in python


def f1(a, b):
    print(f"a = {a}, b = {b}")


f1(3, 4)
f1(30, b=3)
f1(a=2, b=8)

# 36 Difference bettween sorted and sort function
t1 = (34, 64, 32, 79, 88, 32, 93)
s_t1 = sorted(t1)
print(s_t1)
print(type(s_t1))

l1 = [33, 88, 22, 90, 202, 3]
l1.sort()
print(type(l1))
print(l1)

# 37 Static method and variable


class myclass:
    a = 5

    def __init__(self):
        self.x = 10
        y = 4
        myclass.b = 34  # static variable

    def f1(self):
        myclass.c = 65  # static variable

    @staticmethod
    def f2(self):
        myclass.d = 55  # static variable

    @classmethod
    def f3(cls):
        cls.e = 14  # static variable
        myclass.f = 45  # static variable


myclass.g = 11  # static variable

# 38. How to use else with loop in python
i = 20
while i <= 10:
    print(i, end=" ")
    if i == 5:
        break
    i += 1
else:
    print("You are in else")

# 39. what is name mingling in python


class world:
    x = 10
    __india = 20


print(world.x)
print(world._world__india)

# 40. Class object and instance object


class test:
    x = 20

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print(self.a, self.b)


print(test.x)  # class object
t1 = test(4, 5)  # instance object
t1.show()
print(t1.a)
print(t1.b)

# 41.  Init method class, this is a constructor class


class Test1:
    def __init__(self):
        self.a = 10
        self.b = 222


t1 = Test1()
print(t1.a, t1.b)

# 42. What are default arguments in functions


def add(a, b, c=4):
    return a+b+c


s = add(3, 2)
print(f"Result {s}")

# 43. Extract int typee values from a list
my_list = ['abc', 34.56, 32, 4+4j, 'b', 55, 55.3, '80', 180]
print(my_list)
l2 = []
for e in my_list:
    if type(e) == int:
        l2.append(e)
print(l2)


# 44. Python supported inheriatance
class A:
    pass


class B:
    pass


class C(A, B):
    pass


# 45. What is monkey patching
class TestMonkey:
    def __init__(self, x):
        self.a = x

    def get_data(self):
        print('send code to fetch data from database')

    def f1(self):
        self.get_data()

    def f2(self):
        self.get_data()


t1 = TestMonkey(4)
t1.f1()
t1.f2()


def get_new_data(self):
    print('some to code fetch data from test data')


TestMonkey.get_data = get_new_data
print('After Monkey Patching')
t1.f1()
t1.f2()

# 46. Accept a number user check whether it is prime or not
num = 3
for i in range(2, num):
    if num % i == 0:
        print("number is not prime")
        break
else:
    print('number is prime')

# 47. Write a program to print the given numbers is odd or even
num = 30
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 48. Write a program to find the given number is positive or negative
num: float = -33.3
if num > 0:
    print("Number is positive")
elif num == 0:
    print("Number is zero")
else:
    print("Number is negative")

# 49. Write a program to find the sum of two number
num_one = 1
num_two = 2
print(num_one + num_two)


# 50. Write a program to find GCD of two numbers
first_num = 235
second_num = 875


def gcd(a, b):
    if a == 0 or a == b:
        return b
    elif b == 0:
        return a
    elif a > b:
        return gcd(a-b, b)
    return gcd(a, b - a)


print(gcd(first_num, second_num))
