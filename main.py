import time
import numpy as np


# Гномья сортировка
def gnome_sort(array):
    i = 1
    j = 2
    N = len(array)
    while i < N:
        if array[i - 1] <= array[i]:
            i, j = j, j + 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return array


# Пузырьковая
def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff
    return array


def openfile(filename):
    with open(filename, "r") as file:
        num_str = file.readline()
        num_list = list(map(int, num_str.split()))
        print(num_list)
        file.close()
    return num_list


print('Выберите режим работы:')
print("1. Загрузка массива из файла.")
print("2. Генерация случайного массива с указанием \n размера для сравнения времени работы")
print("3. Выход из программы")

while True:
    mode = input()
    if mode == "1":
        print('Введите имя файла из котрого загружаем(в формате name.txt):')
        file_name = input()
        list1 = openfile(file_name)
        print('Введите имя файла в который выводим(в формате name.txt):')
        file_output = input()
        f = open(file_output, 'w')
        sorted_list = gnome_sort(list1)
        for number in sorted_list:
            f.write(f"{number} ")
        #f.write(str(sorted_list))
        f.close()
        print(f"Отсортированный массив:\n{sorted_list}")
    elif mode == "2":
        print("Введите размер массива:")
        n2 = int(input())
        list1 = np.random.randint(0, 1000, size=n2)
        list2 = list1.copy()

        time3 = time.perf_counter()
        sort_list = gnome_sort(list2)
        time4 = time.perf_counter()
        print(f"Гномья сортировка заняла {time4 - time3:0.4f} секунд")

        time1 = time.perf_counter()
        sort_list2 = bubble_sort(list1)
        time2 = time.perf_counter()
        print(f"Пузырьковая сортировка заняла {time2 - time1:0.4f} секунд")

    elif mode == "3":
        print("Выход из программы.")
        break
    else:
        print("Выбран неверный режим работы.")
