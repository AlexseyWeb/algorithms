from threading import Thread 
from time import sleep 

def display(count, text):
    for i in range(0, count):
        sleep(1.5)
        print(f"{i} -> {text}")
t = Thread(target=display, args=(10, "Дочерний поток"))
t.start()
display(10, "Главный поток")
print("Программа завершена.")