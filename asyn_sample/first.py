"""Concurenty thread"""
from threading import Thread
from time import sleep


def some_operation() -> int:
    for i in range(1, 10):
        sleep(1)
        print(f"Функция -> {i}")


if __name__ == '__main__':
    first_thread = Thread(target=some_operation, daemon=True)
    first_thread.start()  # Start function
    for i in range(1, 10, 2):
        print(f"Основной поток -> {i}")
    first_thread.join()  # wait
    print("Конец основного потока")
