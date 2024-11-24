"""Working with modules secrets and string for generation password """
import secrets
import string

all_chars = string.ascii_letters + string.digits + string.punctuation

try:
    number = input("Введите длину пароля (20) -> ")
    print("".join(secrets.choice(all_chars) for i in range(int(number))))
except Exception as err:
    print("Wrong input ")
