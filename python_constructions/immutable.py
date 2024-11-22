""" immutable object """

first = 100
second = first

print(f"{id(first) == id(second)}")

second += 10
print(f"{id(first) == id(second)}")

print(id((1,2,3) == id((1,2,3))))