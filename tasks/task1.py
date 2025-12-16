import random

def sort_desc(arr):
    return sorted(arr, reverse=True)

def sort_asc(arr):
    return sorted(arr)

def sum_arrays_with_zero(a, b):
    return [0 if x == y else x + y for x, y in zip(a, b)]

def solve_task1(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("Массивы должны быть одинаковой длины")
    a_sorted = sort_desc(arr1)
    b_sorted = sort_asc(arr2)
    summed = sum_arrays_with_zero(a_sorted, b_sorted)
    return sort_asc(summed)

def menu():
    arr1 = None
    arr2 = None
    result = None

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
                    result = None  # сброс результата при новых данных
                    print("Данные введены.")
            except ValueError:
                print("Ошибка: введите только целые числа!")
                arr1 = arr2 = None

        elif choice == "2":
            try:
                n = int(input("Размер массивов (целое число): "))
                if n <= 0:
                    print("Размер должен быть положительным!")
                    continue
                arr1 = [random.randint(1, 20) for _ in range(n)]
                arr2 = [random.randint(1, 20) for _ in range(n)]
                result = None  # ← сброс
                print("Сгенерировано:")
                print("Массив 1:", arr1)
                print("Массив 2:", arr2)
            except ValueError:
                print("Ошибка: введите целое число!")

        elif choice == "3":
            if arr1 is None or arr2 is None:
                print("Ошибка: сначала введите данные!")
            else:
                try:
                    result = solve_task1(arr1, arr2)
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