import numpy as np

array = np.arange(0, 10)
print("Исходный массив :")
print(array)

print("\nЭлементы с индексами от 3 до 6 :")
print(array[3:6])

array[7] = 10
array[8] = 20
array[9] = 30
print("\nИзмененный массив :")
print(array)