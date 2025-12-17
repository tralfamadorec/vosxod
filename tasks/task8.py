import random
import logging

# настройка логирования
logger = logging.getLogger("task8")
logger.setLevel(logging.INFO)  # уровень INFO — можно сменить на CRITICAL для отключения

# обработчик: запись в файл
handler = logging.FileHandler("task8.log", encoding="utf-8")
handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s"))

# избегаем дублирования, если модуль импортируется повторно
if not logger.handlers:
    logger.addHandler(handler)
    logger.propagate = False

def reverse_number(n):
    logger.info(f"Вызов reverse_number с аргументом: {n}")
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
    if n < 0:
        raise ValueError("Число должно быть неотрицательным для корректного переворота")
    return int(str(n)[::-1])

def count_common_with_reverse(arr1, arr2):
    if not arr1 or not arr2:
        raise ValueError("Массивы не должны быть пустыми")
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
    logger.info("Вызов count_common_with_reverse")
    for x in arr1:
        if x in arr2 or reverse_number(x) in arr2:
            count += 1
    logger.info(f"Результат подсчёта: {count}")
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
        logger.info(f"Пользователь выбрал пункт меню: {choice}")

        if choice == "1":
            try:
                arr1 = list(map(int, input("Массив 1 (через пробел): ").split()))
                arr2 = list(map(int, input("Массив 2 (через пробел): ").split()))
                result = None  # сброс результата
                logger.info("Данные введены вручную")
            except ValueError as e:
                print("Ошибка: введите только целые числа!")
                logger.error(f"Ошибка ввода вручную в задании 8: {e}")
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
                logger.info(f"Сгенерированы случайные массивы длины {n}")
            except ValueError as e:
                print("Ошибка: введите целое число!")
                logger.error(f"Ошибка генерации данных в задании 8: {e}")

        elif choice == "3":
            if arr1 is None or arr2 is None:
                print("Ошибка: сначала введите данные!")
                logger.info("Отказ: попытка выполнить алгоритм без данных")
            else:
                try:
                    result = count_common_with_reverse(arr1, arr2)
                    print("Алгоритм выполнен.")
                    logger.info("Алгоритм успешно выполнен")
                except ValueError as e:
                    print(f"Ошибка в данных: {e}")
                    logger.error(f"ValueError в count_common_with_reverse: {e}")
                    result = None
                except Exception as e:
                    print(f"Неожиданная ошибка: {e}")
                    logger.error(f"Неожиданное исключение в задании 8: {e}")
                    result = None

        elif choice == "4":
            if result is None:
                print("Ошибка: выполните алгоритм перед выводом!")
                logger.info("Отказ: попытка вывода результата без выполнения")
            else:
                print(f"Общих чисел (с перевёрнутыми): {result}")

        elif choice == "5":
            logger.info("Пользователь вышел из меню задания 8")
            break
        else:
            print("Неверный выбор.")