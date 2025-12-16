import random

def sort_desc(arr):
    """
    сортирует массив по убыванию.

    Args:
        arr (list[int]): исходный список целых чисел.

    Returns:
        list[int]: новый список, отсортированный по убыванию.
    """
    return sorted(arr, reverse=True)


def sort_asc(arr):
    """
    сортирует массив по возрастанию.

    Args:
        arr (list[int]): исходный список целых чисел.

    Returns:
        list[int]: новый список, отсортированный по возрастанию.
    """
    return sorted(arr)


def sum_arrays_with_zero(a, b):
    """
    выполняет поэлементную сумму двух массивов с обнулением совпадающих элементов.
    если элементы на одинаковых позициях равны, их сумма заменяется на 0.
    иначе складываются как обычно.

    Args:
        a (list[int]): первый массив
        b (list[int]): второй массив (должен быть той же длины, что и `a`)

    Returns:
        list[int]: результирующий массив после обработки
    """
    return [0 if x == y else x + y for x, y in zip(a, b)]


def solve(arr1, arr2):
    """
    реализует алгоритм задания 1
    шаги:
    1. Первый массив сортируется по убыванию
    2. Второй массив сортируется по возрастанию
    3. Выполняется поэлементная сумма с обнулением совпадений
    4. Результат сортируется по возрастанию

    Args:
        arr1 (list[int]): первый входной массив
        arr2 (list[int]): второй входной массив (должен быть той же длины)

    Returns:
        list[int]: финальный отсортированный результат

    Raises:
        ValueError: если длины массивов не совпадают
    """
    if len(arr1) != len(arr2):
        raise ValueError("Массивы должны быть одинаковой длины")
    a_sorted = sort_desc(arr1)
    b_sorted = sort_asc(arr2)
    summed = sum_arrays_with_zero(a_sorted, b_sorted)
    return sort_asc(summed)


def menu():
    """
    текстовое меню для задания 1
    пункты меню:
    1. Ввод массивов вручную
    2. Генерация случайных массивов
    3. Выполнение алгоритма
    4. Вывод результата
    5. Возврат в главное меню

    соблюдаются все требования:
    - нельзя выполнить алгоритм без данных
    - нельзя вывести результат без выполнения
    - при вводе новых данных результат сбрасывается (`result = None`)
    - реализованы оба способа ввода: ручной и случайный
    """
    arr1 = None
    arr2 = None
    result = None  # результат недоступен до выполнения

    while True:
        print("\n--- Задание 1 ---")
        print("1. Ввести массивы вручную")
        print("2. Сгенерировать массивы случайно")
        print("3. Выполнить алгоритм")
        print("4. Вывести результат")
        print("5. Назад в главное меню")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            try:
                arr1 = list(map(int, input("Массив 1 (через пробел): ").split()))
                arr2 = list(map(int, input("Массив 2 (через пробел): ").split()))
                if len(arr1) != len(arr2):
                    print("Ошибка: массивы должны быть одинаковой длины!")
                    arr1 = arr2 = None
                else:
                    result = None  # сброс результата
                    print("Данные успешно введены.")
            except ValueError:
                print("Ошибка: введите только целые числа!")
                arr1 = arr2 = None

        elif choice == "2":
            try:
                n = int(input("Размер массивов (целое положительное число): "))
                if n <= 0:
                    print("Размер должен быть больше нуля!")
                    continue
                arr1 = [random.randint(1, 20) for _ in range(n)]
                arr2 = [random.randint(1, 20) for _ in range(n)]
                result = None
                print("Сгенерировано:")
                print("Массив 1:", arr1)
                print("Массив 2:", arr2)
            except ValueError:
                print("Ошибка: введите корректное целое число!")

        elif choice == "3":
            if arr1 is None or arr2 is None:
                print("Ошибка: сначала введите данные!")
            else:
                try:
                    result = solve(arr1, arr2)
                    print("Алгоритм выполнен.")
                except Exception as e:
                    print(f"Ошибка при выполнении: {e}")
                    result = None

        elif choice == "4":
            if result is None:
                print("Ошибка: сначала выполните алгоритм!")
            else:
                print("Результат:", result)

        elif choice == "5":
            break
        else:
            print("Неверный выбор.")