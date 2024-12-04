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
