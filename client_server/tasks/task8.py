import random
import logging
from errors import InvalidInputError, EmptyArrayError, NegativeNumberError, Messages

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
        raise NegativeNumberError(Messages.TASK8_NEGATIVE_NUMBER)
    return int(str(n)[::-1])

def count_common_with_reverse(arr1, arr2):
    if not arr1 or not arr2:
        raise EmptyArrayError(Messages.TASK8_EMPTY_ARRAY)
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
                result = None
                logger.info("Данные введены вручную")
            except ValueError:
                raise InvalidInputError(Messages.INVALID_INPUT_INT)
            except (InvalidInputError, EmptyArrayError, NegativeNumberError) as e:
                print(f"Ошибка в данных: {e}")
                logger.error(f"Ошибка в задании 8: {e}")
                arr1 = arr2 = None

        elif choice == "2":
            try:
                n = int(input("Размер массивов: "))
                if n <= 0:
                    raise InvalidInputError(Messages.INVALID_INPUT_SIZE)
                # ...
            except ValueError:
                raise InvalidInputError(Messages.INVALID_INPUT_INT)
            except InvalidInputError as e:
                print(f"Ошибка ввода: {e}")
                logger.error(f"Ошибка генерации в задании 8: {e}")

        elif choice == "3":
            if arr1 is None or arr2 is None:
                print(Messages.NO_DATA)
                logger.info("Отказ: попытка выполнить алгоритм без данных")
            else:
                try:
                    result = count_common_with_reverse(arr1, arr2)
                    print(Messages.ALGO_DONE)
                    logger.info("Алгоритм успешно выполнен")
                except (EmptyArrayError, NegativeNumberError) as e:
                    print(f"Ошибка в данных: {e}")
                    logger.error(f"Ошибка в задании 8: {e}")
                except Exception as e:
                    print(f"Неожиданная ошибка: {e}")
                    logger.error(f"Неожиданное исключение в задании 8: {e}")
                    result = None


        elif choice == "4":
            if result is None:
                print(Messages.NOT_EXECUTED)
                logger.info("Отказ: попытка вывода результата без выполнения")
            else:
                print(f"{Messages.TASK8_RESULT_PREFIX} {result}")
                logger.info("Результат выведен")
                input("\nНажмите Enter для возврата в меню...")

        elif choice == "5":
            logger.info("Пользователь вышел из меню задания 8")
            break
        else:
            print(Messages.INVALID_CHOICE)