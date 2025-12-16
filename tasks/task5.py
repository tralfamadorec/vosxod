import random

def count_subarrays_with_sum(arr, target):
    """
    подсчитывает количество непрерывных подмассивов, сумма элементов которых равна заданному числу.
    подмассив - это последовательный фрагмент исходного массива.
    алгоритм использует полный перебор всех возможных подмассивов (O(n²)).

    Args:
        arr (list[int]): исходный массив целых чисел.
        target (int): целевая сумма для поиска.

    Returns:
        int: количество подмассивов, сумма которых равна target.

    Examples:
        >>> count_subarrays_with_sum([1, 2, 3], 3)
        2  # подмассивы: [1,2] и [3]
    """
    count = 0
    n = len(arr)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == target:
                count += 1
    return count


def menu():
    """
    текстовое меню для задания 5
    позволяет пользователю:
    - ввести массив и целевое число вручную,
    - сгенерировать случайные данные,
    - выполнить алгоритм,
    - вывести результат.

    соблюдаются все требования:
    - алгоритм недоступен без ввода данных,
    - результат недоступен без выполнения,
    - при вводе новых данных результат сбрасывается.
    """
    arr = None
    target = None
    result = None  # результат не определён до выполнения

    while True:
        print("\n--- Задание 5 ---")
        print("1. Ввести массив и число вручную")
        print("2. Сгенерировать данные случайно")
        print("3. Выполнить алгоритм")
        print("4. Вывести результат")
        print("5. Назад в главное меню")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            try:
                arr = list(map(int, input("Массив (через пробел): ").split()))
                target = int(input("Целевое число: "))
                result = None  # сброс результата
                print("Данные успешно введены.")
            except ValueError:
                print("Ошибка: введите только целые числа!")
                arr = target = None

        elif choice == "2":
            try:
                n = int(input("Размер массива (целое положительное число): "))
                if n <= 0:
                    print("Размер должен быть больше нуля!")
                    continue
                arr = [random.randint(-10, 10) for _ in range(n)]
                target = random.randint(-5, 10)
                result = None
                print("Сгенерировано:")
                print("Массив:", arr)
                print("Целевое число:", target)
            except ValueError:
                print("Ошибка: введите корректное целое число!")

        elif choice == "3":
            if arr is None or target is None:
                print("Ошибка: сначала введите данные!")
            else:
                result = count_subarrays_with_sum(arr, target)
                print("Алгоритм выполнен.")

        elif choice == "4":
            if result is None:
                print("Ошибка: сначала выполните алгоритм!")
            else:
                print(f"Количество подмассивов с суммой {target}: {result}")

        elif choice == "5":
            break
        else:
            print("Неверный выбор.")