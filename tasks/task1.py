import random
import logging


# настройка логгера
logger = logging.getLogger("task1")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("task1.log", encoding="utf-8")
handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s"))

if not logger.handlers:
    logger.addHandler(handler)
    logger.propagate = False


def sort_desc(arr):
    """
    сортирует массив по убыванию.

    Args:
        arr (list[int]): исходный список целых чисел.

    Returns:
        list[int]: новый список, отсортированный по убыванию.
    """
    logger.info(f"Вызов sort_desc с массивом: {arr}")
    return sorted(arr, reverse=True)


def sort_asc(arr):
    """
    сортирует массив по возрастанию.

    Args:
        arr (list[int]): исходный список целых чисел.

    Returns:
        list[int]: новый список, отсортированный по возрастанию.
    """
    logger.info(f"Вызов sort_asc с массивом: {arr}")
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
    logger.info("Вызов sum_arrays_with_zero")
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
    logger.info("Вызов solve: начало обработки")
    a_sorted = sort_desc(arr1)
    b_sorted = sort_asc(arr2)
    summed = sum_arrays_with_zero(a_sorted, b_sorted)
    logger.info(f"Алгоритм завершён. Результат: {sort_asc(summed)}")
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
        logger.info(f"Пользователь выбрал пункт меню: {choice}")

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
                    logger.info("Данные введены вручную")
            except ValueError:
                print("Ошибка: введите только целые числа!")
                logger.info("Отказ: попытка выполнить алгоритм без данных")
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
                logger.info(f"Сгенерированы случайные массивы длины {n}")
            except ValueError:
                print("Ошибка: введите корректное целое число!")
                logger.info("Отказ: попытка выполнить алгоритм без данных")

        elif choice == "3":
            if arr1 is None or arr2 is None:
                print("Ошибка: сначала введите данные!")
                logger.info("Отказ: попытка выполнить алгоритм без данных")
            else:
                try:
                    result = solve(arr1, arr2)
                    print("Алгоритм выполнен.")
                    logger.info("Алгоритм успешно выполнен")
                except Exception as e:
                    print(f"Ошибка при выполнении: {e}")
                    logger.info(f"Ошибка при выполнении: {e}")
                    result = None

        elif choice == "4":
            if result is None:
                print("Ошибка: сначала выполните алгоритм!")
                logger.info("Отказ: попытка вывода результата без выполнения")
            else:
                print("Результат:", result)
                logger.info("Результат выведен")

        elif choice == "5":
            logger.info("Пользователь вышел из меню задания 1")
            break
        else:
            print("Неверный выбор.")