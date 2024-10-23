
import threading
def calc_kvadrat (x:int) -> None:
    for i in range(1,x+1):
        print (f"...Квадрат числа {i}: {i*i}")

def calc_kub (x:int) -> None:
    for i in range(1,x+1):
        print (f".Куб числа {i}: {i*i*i}")


if __name__ == "__main__":

    thread1 = threading.Thread(target=calc_kvadrat, args=[10])
    thread2 = threading.Thread(target=calc_kub, args=[10])

    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()









# import threading

# def calculate_squares():
#     for i in range(1, 11):
#         print(f"Квадрат числа {i}: {i*i}")

# def calculate_cubes():
#     for i in range(1, 11):
#         print(f"Куб числа {i}: {i*i*i}")

# if __name__ == "__main__":
#     thread1 = threading.Thread(target=calculate_squares)
#     thread2 = threading.Thread(target=calculate_cubes)
    
#     thread1.start()
#     thread2.start()
    
#     thread1.join()
#     thread2.join()









    # thread1 = threading.Thread(target=calc_kvadrat, args=(10,))
    # thread2 = threading.Thread(target=calc_kub, args=(10,))

    # thread1.start()
    # thread2.start()

    # thread1.join()
    # thread2.join()

# def calculate_squares():
# /*************  ✨ Codeium Command ⭐  *************/
#     """
#     Выводит на экран квадраты целых чисел от 1 до 10.
#     """
# /******  896c3be2-30e6-479a-8a94-90e7af20cfd3  *******/
#     for i in range(1, 11):
#         print(f"Квадрат числа {i}: {i*i}")

# def calculate_cubes():
#     for i in range(1, 11):
#         print(f"Куб числа {i}: {i*i*i}")

# if __name__ == "__main__":
#     thread1 = threading.Thread(target=calculate_squares)
#     thread2 = threading.Thread(target=calculate_cubes)
    
#     thread1.start()
#     thread2.start()
    
#     thread1.join()
#     thread2.join()







# def kvadrat (x:int) -> int:
#     for i in range(1,x+1):
#         p = i*i
#         print (f"{i} ^2 = {p}")
#     return p

# def kub (x:int) -> int:
#     for i in range(1,x+1):
#         s = i*i*i
#         print (f"{i} ^2 = {s}")
#     return s


# x = int(5)
# print (f"Квардрат числа {x}: {kvadrat(x)}")
# print (f"Куб числа {x}: {kub(x)}")

