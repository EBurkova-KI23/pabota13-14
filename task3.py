from task2 import rotate_matrix


def task3():
    """Выполняет задание 3: Поворот матрицы."""

    while True:
        print("\nЗадание 3: Поворот матрицы")

        rows = int(input("Введите количество строк матрицы: "))
        if rows.lower() == 'exit':
            break
        cols = int(input("Введите количество столбцов матрицы: "))

        matrix = []

        for i in range(rows):
            row = list(map(int, input(f"Введите элементы строки {i + 1} через пробел: ").split()))
            matrix.append(row)

        direction = input("Введите направление поворота (по часовой стрелке/против часовой стрелки): ")

        if direction.lower() == "против часовой стрелки":
            matrix = rotate_matrix(matrix)
            matrix = rotate_matrix(matrix)
            matrix = rotate_matrix(matrix)

        elif direction.lower() == "по часовой стрелке":
            matrix = rotate_matrix(matrix)

        else:
            print("Неверное направление поворота.")
            continue

        print("Повернутая матрица:")
        for row in matrix:
            print(" ".join(map(str, row)))