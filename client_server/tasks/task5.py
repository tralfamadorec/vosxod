import random
import logging
from errors import InvalidInputError, EmptyArrayError, Messages

# настройка логгера
logger = logging.getLogger("task5")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("task5.log", encoding="utf-8")
handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s"))

if not logger.handlers:
    logger.addHandler(handler)
    logger.propagate = False

def count_subarrays_with_sum(arr, target):
    if not arr:
        raise ValueError("Массив не должен быть пустым")
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
    logger.info(f"Вызов count_subarrays_with_sum с массивом {arr} и целью {target}")
    if not arr:
        raise EmptyArrayError(Messages.TASK5_EMPTY_ARRAY)
    count = 0
    n = len(arr)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == target:
                count += 1
    logger.info(f"Найдено подмассивов: {count}")
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
        logger.info(f"Пользователь выбрал пункт меню: {choice}")

        if choice == "1":
            try:
                arr = list(map(int, input("Массив (через пробел): ").split()))
                target = int(input("Целевое число: "))
                if not arr:
                    raise EmptyArrayError(Messages.TASK5_EMPTY_ARRAY)
                result = None
                print(Messages.DATA_ENTERED)
            except ValueError:
                raise InvalidInputError(Messages.INVALID_INPUT_INT)
            except (InvalidInputError, EmptyArrayError) as e:
                print(f"Ошибка в данных: {e}")
                logger.error(f"Ошибка в задании 5: {e}")
                arr = target = None

        elif choice == "2":
            try:
                n = int(input("Размер массива (целое положительное число): "))
                if n <= 0:
                    print(Messages.INVALID_INPUT_SIZE)
                    continue
                arr = [random.randint(-10, 10) for _ in range(n)]
                target = random.randint(-5, 10)
                result = None
                print(Messages.GENERATED)
                print("Массив:", arr)
                print("Целевое число:", target)
                logger.info(f"Сгенерированы случайные данные: массив длины {n}, цель = {target}")
            except ValueError as e:
                print(Messages.INVALID_INPUT_INT)
                logger.error(f"Ошибка генерации данных в задании 5: {e}")


        elif choice == "3":
            if arr is None or target is None:
                print(Messages.NO_DATA)
                logger.info("Отказ: попытка выполнить алгоритм без данных")
            else:
                try:
                    result = count_subarrays_with_sum(arr, target)
                    print(Messages.ALGO_DONE)
                except EmptyArrayError as e:
                    print(f"Ошибка: {e}")
                    logger.error(f"EmptyArrayError: {e}")
                    result = None


        elif choice == "4":
            if result is None:
                print(Messages.NOT_EXECUTED)
                logger.info("Отказ: попытка вывода без выполнения")
            else:
                print(f"{Messages.TASK5_RESULT_PREFIX} {target}: {result}")
                logger.info("Результат выведен")
                input("\nНажмите Enter для возврата в меню...")

        elif choice == "5":
            logger.info("Пользователь вышел из меню задания 5")
            break
        else:
            print(Messages.INVALID_CHOICE)