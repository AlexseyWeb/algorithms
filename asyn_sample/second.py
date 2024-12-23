"""submit """

from concurrent.futures import ThreadPoolExecutor
from time import sleep


def some_operation() -> int:
    for i in range(1, 10):
        sleep(1)
        print(f"Функция -> {i}")


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executer:
        executer.submit(some_operation)
    for i in range(1, 10):
        print(f"Main loop -> {i}")
