import random

def count_subarrays_with_sum(arr, target):
    count = 0
    n = len(arr)
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s == target:
                count += 1
    return count

def menu():
    arr = None
    target = None
    result = None

    while True:
        print("\n--- Задание 5 ---")
        print("1. Ввести массив и число")
        print("2. Сгенерировать случайные данные")
        print("3. Выполнить алгоритм")
        print("4. Вывести результат")
        print("5. Назад в главное меню")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            try:
                arr = list(map(int, input("Массив (через пробел): ").split()))
                target = int(input("Целевое число: "))
                result = None
            except:
                print("Ошибка: введите только целые числа!")
                arr = target = None

        elif choice == "2":
            try:
                n = int(input("Размер массива: "))
                if n <= 0:
                    print("Размер должен быть > 0")
                    continue
                arr = [random.randint(-5, 10) for _ in range(n)]
                target = random.randint(1, 10)
                result = None
                print("Сгенерировано:")
                print("Массив:", arr)
                print("Целевое число:", target)
            except:
                print("Ошибка: введите целое число!")

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
                print(f"Количество подмассивов: {result}")

        elif choice == "5":
            break
        else:
            print("Неверный выбор.")