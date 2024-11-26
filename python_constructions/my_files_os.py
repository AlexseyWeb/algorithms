from pathlib import Path
import json
from termcolor import colored

file_path = Path("test.txt")
statics_file = Path("main.py").stat()
print([m for m in dir(file_path) if not m.startswith("_")])
print(statics_file)

# All files and directory in folder
for i in Path(".").iterdir():
    if not i.is_dir():
        print(f"File ... -> {colored(i, "green")}")
    else:
        print(f"Directory ... -> {colored(i, "light_magenta")}")


print(colored("-" * 30, "white"))
with open("my_json.py") as file:
    for line in file.readlines():
        print(colored(json.dumps(line), "red"))
