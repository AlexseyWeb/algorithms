""" Создание временного файла """

import tempfile

with tempfile.NamedTemporaryFile(delete=False) as t:
    t.write(b"template file")
    path = t.name 
    print(path)

with open(path) as t:
    print(t.read())