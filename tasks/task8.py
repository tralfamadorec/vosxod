import random

def reverse_number(n):
    return int(str(n)[::-1])

def count_common_with_reverse(a, b):
    count = 0
    for x in a:
        if x in b or reverse_number(x) in b:
            count += 1
    return count

def menu():
    arr1 = None
    arr2 = None
    result = None

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
                result = None
            except:
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
            except:
                print("Ошибка: введите целое число!")

        elif choice == "3":
            if arr1 is None or arr2 is None:
                print("Ошибка: введите данные!")
            else:
                result = count_common_with_reverse(arr1, arr2)
                print("Алгоритм выполнен.")

        elif choice == "4":
            if result is None:
                print("Ошибка: выполните алгоритм!")
            else:
                print(f"Общих чисел (с перевёрнутыми): {result}")

        elif choice == "5":
            break
        else:
            print("Неверный выбор.")