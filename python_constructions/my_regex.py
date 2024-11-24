""" Working with module re"""
import re

my_name = "My name is Alexsey!"

result = re.search(r'A.....y!$', my_name)
print(result)

# Check email on validate


def check_email(email):
    email_regex = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_pattern = re.compile(email_regex)
    result = "Valid" if email_check_pattern.fullmatch(email) else "Not Valid"
    return (email, result)


print(check_email("sample.internet@gmail.com"))
print(check_email("sample@mail.ru"))
print(check_email("wrong@yandex.ru"))
print(check_email("ssory_333@mail.ru"))
print(check_email("3333_~@mail.ru"))
