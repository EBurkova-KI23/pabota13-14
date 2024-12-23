from task1 import task1
from task2 import task2
from task3 import task3
import threading


def print_menu():
    """Выводит меню с доступными заданиями."""
    print("\nМеню:")
    print("1. Ввод исходных данных")
    print("2. Выполнение алгоритма")
    print("3. Вывод результата")
    print("4. Завершение работы программы")


def main():
    """Основная функция программы, которая управляет выбором задания пользователем."""
    while True:
        print_menu()  # Выводим меню
        choice = input("Выберите пункт меню: ")  # Запрашиваем выбор пользователя

        if choice == '1':
            thread = threading.Thread(target=task1)
            thread.start()  # Запускаем задание 1 в новом потоке
            thread.join()  # Ожидаем завершения потока

        elif choice == '2':
            thread = threading.Thread(target=task2)
            thread.start()  # Запускаем задание 2 в новом потоке
            thread.join()  # Ожидаем завершения потока

        elif choice == '3':
            thread = threading.Thread(target=task3)
            thread.start()  # Запускаем задание 3 в новом потоке
            thread.join()  # Ожидаем завершения потока

        elif choice == '4':
            print("Завершение работы программы.")  # Сообщаем о завершении
            break  # Выходим из цикла

        else:
            print("Неверный выбор.")  # Обработка неверного выбора

        input("Нажмите Enter, чтобы продолжить...")  # Пауза перед повторным выводом меню


if __name__ == "__main__":
    main()  # Запуск основной функции при выполнении скрипта