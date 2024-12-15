def task2():
    """Меню второго задания."""
    while True:
        print("\nЗадание 2: Проверка сумм трёх массивов")

        array_input_1 = input("Введите элементы первого массива через пробел: ")
        if array_input_1.lower() == 'exit':
            break

        array_input_2 = input("Введите элементы второго массива через пробел: ")

        array_input_3 = input("Введите элементы третьего массива через пробел: ")

        try:
            arr1 = list(map(int, array_input_1.split()))
            arr2 = list(map(int, array_input_2.split()))
            arr3 = list(map(int, array_input_3.split()))

            if len(arr1) != len(arr2) or len(arr2) != len(arr3):
                print("Все массивы должны быть одинакового размера.")
                continue

            results = []  # Список для хранения результатов

            for a, b, c in zip(arr1, arr2, arr3):
                if a + b == c:
                    results.append((a + b + c) ** min(a, b, c))

            print("Результаты:", results)  # Выводим результаты проверки сумм

        except ValueError:
            print("Ошибка ввода. Убедитесь, что введены только числа.")


import math


def rotate_matrix(matrix):
    """Поворачивает матрицу на 90 градусов против часовой стрелки."""
    return [list(reversed(col)) for col in zip(*matrix)]