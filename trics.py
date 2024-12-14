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

# 51 Write a program to pritn
total_star = 5
for i in range(1, total_star+1):
    print("* " * i)
    i += 1

# 52. Write a program
number = 4
for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    i += 1

# 53. Write a program


def tri(n):
    num = 1
    for i in range(0, n):
        for j in range(0, i+1):
            print(num, end=" ")
            num += 1
        print()


tri(5)

# 54. Write a program


def apha(n):
    p = 65
    for i in range(n):
        for j in range(i + 1):
            ch = chr(p)
            print(ch, end=" ")
        p += 1
        print()


apha(5)

# 55. Write a program


def alpha(n):
    p = 65
    for i in range(n):
        for j in range(i+1):
            ch = chr(p)
            p += 1
            print(ch, end=" ")
        print()


alpha(5)

# 56. Write pyramid


def pyramid_chars(n):
    num = 65
    for i in range(n):
        for j in range(i, n):
            print(" ", end="")
        for j in range(i+1):
            print(chr(num), end=" ")
            num += 1
        num = 65
        print()


pyramid_chars(5)

# 57. Write chars pyramid


def chars_pyramid(n):
    num = 65
    for i in range(n + 1):
        for j in range(n-i):
            print(" ", end="")
        for j in range(1, i+1):
            print(chr(num), end=" ")
            num += 1
        print("")


chars_pyramid(6)

# 58. Create a sandglass pattern


def sandglass(n):
    n = 5
    for i in range(n):
        for j in range(i+1):
            print("", end=" ")
        for j in range(i, n):
            print("*", end=" ")
        print()
    for i in range(n):
        for j in range(i, n):
            print("", end=" ")
        for j in range(i+1):
            print("*", end=" ")
        print()


sandglass(6)

# 59. Create a reverse pyramid pattern


def reverse_pyramid(n):
    for i in range(n):
        for j in range(i+1):
            print(" ", end="")
        for j in range(i, n):
            print("*", end=" ")
        print()


print()
reverse_pyramid(5)

# 60. Square matrix


def square_matrix(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


square_matrix(5)

# 61. Parallel vertical lines


def draw_parallel_line():
    n = 9
    for i in range(n):
        for j in range(n):
            if j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


draw_parallel_line()
print()
# 62. square plus pattern


def draw_square_pattern():
    n = 9
    for i in range(n):
        for j in range(n):
            if i == n//2 or j == n//2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


draw_square_pattern()

# 63. Cross pattern


def draw_cross_pattern():
    n = 9
    for i in range(n):
        for j in range(n):
            if i == j or i+j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


draw_cross_pattern()
print()
# 64. hollow square pattern


def draw_hollow_squar_pattern():
    n = 9
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=".")
        print()


draw_hollow_squar_pattern()

# 65 Check if a number is palindrome or not


def isPalindrom():
    n = 1001
    m = n
    sum = 0
    while m != 0:
        d = m % 10
        sum = sum * 10 + d
        m = m // 10
    if sum == n:
        print("Yes")
    else:
        print("No")


isPalindrom()

# 66 Check if a number is spy number


def isSpyNumber():
    n = 132
    m = n
    sum = 0
    prod = 1
    while m != 0:
        d = m % 10
        m = m//10
        sum = sum + d
        prod = prod * d
    if sum == prod:
        print("Yes")
    else:
        print("No")


isSpyNumber()

# 67. Check if a number is Krishna Murthy


def check_krishna():
    import math
    n = 145
    m = n
    sum = 0
    while m != 0:
        d = m % 10
        sum = sum + math.factorial(d)
        m = m // 10
    if sum == n:
        print("Yes")
    else:
        print("No")


check_krishna()

# 68. Find the factors of a number


def find_factors():
    n = int(input("Enter a number: "))
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")


# find_factors()

# 69. Find if the number is pronic or not.
def find_pronic():
    n = int(input("Enter a number: "))
    fact = 0
    for i in range(1, n+1):
        if (i*(i+1) == n):
            print(f"{i} x {i+1} = {n}")
            fact = i
    if fact > 0:
        print("Pronic number")
    else:
        print("Not a Pronic number ")


# find_pronic()

# 70 Arithematic series


def arithematic_sequence():
    n = int(input("Enter a number: "))
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    print('Sum of series: ', sum)


# arithematic_sequence()

# 71. sequesnce
def sequence():
    n = 20
    sum = 0
    a = 2
    for i in range(1, n+1):
        sum = sum + a
        a += 2
    print('Sum of seriws: ', sum)


sequence()

# 72. sequence qwadro


def sequence_power():
    n = 10
    x = 3
    sum = 0
    a = 10
    for i in range(1, n+1):
        sum = sum + x ** i
    print('Sum of series: ', sum)


sequence_power()

# 73. sequence factorial


def sequence_factorial():
    n = 20
    x = 2
    sum = 0
    a = 2
    for i in range(1, n+1):
        sum = sum + a ** x
        a += 2
    print('Sum of series: ', sum)


sequence_factorial()

# 74. sequence sample


def sequence_other():
    n = 20
    x = 2
    sum = 0
    a = 1
    for i in range(1, n+1):
        sum = sum + (a**3) / x
        a += 2
    print('Sum of series: ', sum)


sequence_other()

# 75. 2/10 + 4/9 + 6/8 + 8/7


def sequence_names():
    n = 10
    sum = 0
    a = 2
    b = 10
    for i in range(1, n+1):
        sum = sum + a/b
        a += 2
        b -= 1
    print('Sum of series: ', sum)


sequence_names()

# 76. Geometrix series


def geometrix_sequence():
    n = 20
    sum = 0
    a = 2
    for i in range(1, n+1):
        sum = sum + a * 2
        a = a * 2
    print('Sum of series: ', sum)


geometrix_sequence()

# 77. geometrix 3


def geometrix_three():
    n = 20
    sum = 0
    a = 10
    for i in range(1, n+1):
        sum = sum + a
        a = a * 3
    print('Sum of series: ', sum)


geometrix_three()

# 78. Geometrix other


def geometrix_other():
    n = 10
    sum = 0
    a = 5
    for i in range(1, n+1):
        sum = sum + a
        a = a * 3
    print('Sum of series: ', sum)

# 79. geometrix two


def geometrix_second():
    n = 10
    x = 2
    sum = 0
    a = 2
    for i in range(1, n+1):
        sum = sum + x / a
        a = a * 2
    print('Sum of series: ', sum)


geometrix_second()

# 80. geometrix (x+2)/ 10 + (x+4)/ 30


def geometrix_party():
    n = 20
    sum = 0
    a = 2
    for i in range(1, n+1):
        if i % 2 == 0:
            sum = sum - a
        else:
            sum = sum + a
        a = a * 3
    print('Sum of series: ', sum)


geometrix_party()
# 81. sequence algoritm


def sequence_algoritm():
    n = 10
    x = 2
    a = 2
    sum = 0
    b = 10
    for i in range(1, n+1):
        sum = sum+(x+a) / b
        a += 2
        b = b*3
    print('Sum of series: ', sum)


sequence_algoritm()

# 82. convert numbered string by reversing


def convert_to_reversing_string():
    s = '83838837726'
    s = s[::-1]
    print(s)
    i = 0
    res = ""
    while (i < len(s) - 1):
        x = s[i]+s[i+1]
        if x == '32':
            res = res + " "
        elif int(x) in range(65, 91) or int(x) in range(97, 123):
            res = res + chr(int(x))
        elif i + 2 < len(s):
            x = x + s[i+2]
            res = res + chr(int(x))
            i += 1
        i += 2
    print(res)


convert_to_reversing_string()

# 83 What are the commonly used decorators in python


class MyClass:
    a = 'I am a class variable'

    def __init__(self, len):
        self.length = len

    @classmethod
    def class_method(cls):
        print('This is a class method')
        print(f'using class variable: {cls.a}')


# using class method without creating an instance
MyClass.class_method()

# 84. classmethod example


class InstanceCounter:
    count = 0

    def __init__(self):
        InstanceCounter.count += 1

    @classmethod
    def get_instance_count(cls):
        return cls.count


# Creating instance
obj1 = InstanceCounter()
obj2 = InstanceCounter()
total_instance = InstanceCounter.get_instance_count()
print(f'Total number of instance created: {total_instance}')

# 85. Static method


class MyClass:
    class_variable = 'I am a class variable'

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @staticmethod
    def static_method():
        print('This is a static method')
        print('It does not have access to instance variables or self.')


MyClass.static_method()

# 86.  static method calculator code


class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            print("Cannot divide by zero")
            return None


# using the static methdos without createing an instance
result_add = Calculator.add(3, 32)
result_subtract = Calculator.subtract(30, 10)
result_multiply = Calculator.multiply(10, 22)
result_divide = Calculator.divide(40, 20)
print(result_add, result_subtract, result_multiply, result_divide)
