import threading
import time

def print_numbers():
    for i in range(1, 11):
        print(i)
time.sleep(1)

# Создаем два потока для выполнения функции print_numbers

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Запускаем потоки

thread1.start()
thread2.start()

# Ждем завершения потоков

thread1.join()
thread2.join()
