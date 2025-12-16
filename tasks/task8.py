import random

def reverse_number(n):
    return int(str(n)[::-1])

def count_common_with_reverse(arr1, arr2):
    count = 0
    for x in arr1:
        if x in arr2 or reverse_number(x) in arr2:
            count += 1
    return count

def menu():
    arr1 = None
    arr2 = None
    result = None

    while True:
        print("\n--- Задание 8 ---")
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
                result = None  # ← сброс при новых данных
                print("Данные введены.")
            except ValueError:
                print("Ошибка: введите только целые числа!")
                arr1 = arr2 = None

        elif choice == "2":
            try:
                n = int(input("Размер массивов (целое положительное число): "))
                if n <= 0:
                    print("Размер должен быть > 0")
                    continue
                # генерируем числа от 10 до 999, чтобы было что переворачивать
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
                try:
                    result = count_common_with_reverse(arr1, arr2)
                    print("Алгоритм выполнен.")
                except Exception as e:
                    print(f"Ошибка при выполнении: {e}")
                    result = None

        elif choice == "4":
            if result is None:
                print("Ошибка: сначала выполните алгоритм!")
            else:
                print(f"Количество общих чисел (с учётом перевёрнутых): {result}")

        elif choice == "5":
            break

        else:
            print("Неверный выбор.")