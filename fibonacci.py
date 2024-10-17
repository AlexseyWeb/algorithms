""" Числа Фибоначи """

count_numbers = 15
first, second = 1, 1

print(first, second, end=" ")

for i in range(count_numbers-2):
    first, second = second, first + second
    print(second, end=" ")

print()

#Итеративный динамический подход
def fibonacci(n):
    memo = [1, 1]

    for i in range(2, n+1):
        memo.append(memo[i-1] + memo[i-2])
        
    return memo[n]

print(f" Сумма 15-го числа Фибоначи => {fibonacci(15)}")
