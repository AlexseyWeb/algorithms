class Image:
    """A simple class on Python
    """

    def __init__(self, title: str, resolution: str, extension: str) -> None:
        self.title = title
        self.resolution = resolution
        self.extension = extension

    def resize(self, width: int, height: int) -> str:
        self.resolution = f"{width}x{height}"
        return self.resolution

    def upper_title(self) -> str:
        txt = self.title.upper()
        return txt

    @staticmethod
    def about_info(name: str, sallary: str) -> None:
        print(f"{name} -> {sallary}")


png = Image("First_image", "1920x1080", '.png')
png.about_info("Alexsey", '183000руб')
Image.about_info("Sergey", "100000")

print(png.resolution)
png.resize(100, 200)
print(png.resolution)

print(png.upper_title())


class ExtendedList(list):
    def info(self):
        return f"List has {len(self)} elements"


numbers_lsit = ExtendedList([1, 2, 3, 4, 5,])
print(numbers_lsit.index(3))
print(numbers_lsit.info())
print(list.__subclasses__())
