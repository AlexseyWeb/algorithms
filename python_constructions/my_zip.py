"""Working with archives"""

from zipfile import ZipFile
from pathlib import Path


def created_directory_and_files(name_directory):
    Path(name_directory).mkdir()

    with open(f"{name_directory}/readme.txt", "w") as file:
        file.write("This is created file to converted zip archive")

    with open(f"{name_directory}/readme-ru.txt", "w", encoding="utf-8") as file:
        file.write("Создание архивов из файлов и каталога.")


# created_directory_and_files("soso")

# with ZipFile("my-files.zip", mode="w") as zip:
#     for file in Path("archives").iterdir():
#         zip.write(file)
#         print(zip)

with ZipFile("my-files.zip", mode="r") as zip:
    print(zip.infolist())
