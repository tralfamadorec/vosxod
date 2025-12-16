import random

def count_subarrays_with_sum(arr, target):
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
    arr = None
    target = None
    result = None

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
                result = None  # сброс при новых данных
                print("Данные введены.")
            except ValueError:
                print("Ошибка: введите только целые числа!")
                arr = target = None

        elif choice == "2":
            try:
                n = int(input("Размер массива (целое положительное число): "))
                if n <= 0:
                    print("Размер должен быть > 0")
                    continue
                arr = [random.randint(-10, 10) for _ in range(n)]
                target = random.randint(-5, 10)
                result = None
                print("Сгенерировано:")
                print("Массив:", arr)
                print("Целевое число:", target)
            except ValueError:
                print("Ошибка: введите целое число!")

        elif choice == "3":
            if arr is None or target is None:
                print("Ошибка: сначала введите данные!")
            else:
                try:
                    result = count_subarrays_with_sum(arr, target)
                    print("Алгоритм выполнен.")
                except Exception as e:
                    print(f"Ошибка при выполнении: {e}")
                    result = None

        elif choice == "4":
            if result is None:
                print("Ошибка: сначала выполните алгоритм!")
            else:
                print(f"Количество подмассивов с суммой {target}: {result}")

        elif choice == "5":
            break

        else:
            print("Неверный выбор.")