"""Working with dictionary """

mans = {
        'name': 'Alexsey',
        'age': 28,
        'job': 'freelancer',
        }

mans['sallary'] = 20000

mans['family'] = ['father', 'mother', 'brother', 'sister']

#Copy dictionary
man = mans.copy()

print(mans.get('name', 'Ghost'))
print(mans)
print(man)

print("Objects equals -> ",id(man) == id(mans))
print(f"Objects keys == {man == mans}")

print(id(mans))
print(type(mans))

print(mans.__doc__)
print(f"All attributes of object -> {dir(mans)}")

#Unpacking dictionary
first_element, *other = man 
print(first_element, other)

characters_dict = {key: value for key, value in enumerate(range(1, 20))}
print(characters_dict)