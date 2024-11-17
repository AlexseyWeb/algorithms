""" Working with Exceptions """

try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)
    print(dir(e))
    print(isinstance(e, ZeroDivisionError))
except TypeError as e:
    print(e)
else:
    print("Errors was not found!")
finally:
    print("Always run!")


def image_info(img):
    if ('image_id' not in img) or ('image_title' not in img):
        raise TypeError(f"Keys 'image_id' and 'image_title' must be present")
    return f"Image {img['image_title']} has id {img['image_id']}"


output = image_info({'image_id': 8, 'image_title': 'Book'})
print(output)

try:
    output = image_info({'image_id': 8})
    print(output)
except TypeError as e:
    print(e)

print("Continue....")
