"""Working with dictionary """

mans = {
        'name': 'Alexsey',
        'age': 28,
        'job': 'freelancer',
        }

mans['sallary'] = 20000

mans['family'] = ['father', 'mother', 'brother', 'sister']

print(mans.get('name', 'Ghost'))
print(mans)

print(id(mans))
print(type(mans))

print(mans.__doc__)
print(f"All attributes of object -> {dir(mans)}")
