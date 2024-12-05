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
