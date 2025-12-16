import random


def reverse_number(n):
    """
    возвращает целое число, полученное переворотом цифр исходного числа.
    пример: 123 -> 321, 100 -> 1 (лидирующие нули отбрасываются)

    Args:
        n (int): исходное целое число (положительное)

    Returns:
        int: перевёрнутое число

    Raises:
        ValueError: если входное значение не является целым числом
    """
    return int(str(n)[::-1])


def count_common_with_reverse(arr1, arr2):
    """
    считает количество элементов из первого массива, которые:
    - присутствуют во втором массиве, ИЛИ
    - их перевёрнутая версия присутствует во втором массиве
    пример:
        arr1 = [123, 45], arr2 = [321, 67] -> общие: 123 (т.к. 321 в arr2)

    Args:
        arr1 (list[int]): первый массив целых чисел
        arr2 (list[int]): второй массив целых чисел

    Returns:
        int: количество "общих" чисел с учётом перевёрнутых версий
    """
    count = 0
    for x in arr1:
        if x in arr2 or reverse_number(x) in arr2:
            count += 1
    return count


def menu():
    """
    реализует текстовое меню для задания 8
    пункты меню:
    1. Ввод массивов вручную
    2. Генерация случайных массивов
    3. Выполнение алгоритма
    4. Вывод результата
    5. Возврат в главное меню

    соблюдаются все требования:
    - нельзя выполнить без данных
    - нельзя вывести без выполнения
    - при новых данных результат сбрасывается
    """
    arr1 = None
    arr2 = None
    result = None  # результат не определён до выполнения

    while True:
        print("\n--- Задание 8 ---")
        print("1. Ввести массивы вручную")
        print("2. Сгенерировать случайно")
        print("3. Выполнить алгоритм")
        print("4. Вывести результат")
        print("5. Назад в главное меню")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            try:
                arr1 = list(map(int, input("Массив 1 (через пробел): ").split()))
                arr2 = list(map(int, input("Массив 2 (через пробел): ").split()))
                result = None  # сброс результата
            except ValueError:
                print("Ошибка: введите только целые числа!")
                arr1 = arr2 = None

        elif choice == "2":
            try:
                n = int(input("Размер массивов: "))
                if n <= 0:
                    print("Размер должен быть > 0")
                    continue
                arr1 = [random.randint(10, 999) for _ in range(n)]
                arr2 = [random.randint(10, 999) for _ in range(n)]
                result = None
                print("Сгенерировано:")
                print("Массив 1:", arr1)
                print("Массив 2:", arr2)
            except ValueError:
                print("Ошибка: введите целое число!")

        elif choice == "3":
            if arr1 is None or arr2 is None:
                print("Ошибка: сначала введите данные!")
            else:
                result = count_common_with_reverse(arr1, arr2)
                print("Алгоритм выполнен.")

        elif choice == "4":
            if result is None:
                print("Ошибка: выполните алгоритм перед выводом!")
            else:
                print(f"Общих чисел (с перевёрнутыми): {result}")

        elif choice == "5":
            break
        else:
            print("Неверный выбор.")