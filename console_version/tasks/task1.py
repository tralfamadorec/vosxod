import random
import logging
from errors import ArraysLengthMismatchError, InvalidInputError, Messages


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
        raise ArraysLengthMismatchError(Messages.TASK1_ARRAYS_LEN_MISMATCH)
    logger.info("Вызов solve: начало обработки")
    a_sorted = sort_desc(arr1)
    b_sorted = sort_asc(arr2)
    summed = sum_arrays_with_zero(a_sorted, b_sorted)
    logger.info(f"Алгоритм завершён. Результат: {sort_asc(summed)}")
    return sort_asc(summed)


def menu():
    # меню задания 1, реализованное через конечный автомат (FSM) с использованием словаря.
    from errors import InvalidInputError, ArraysLengthMismatchError, Messages
    import random

    # контекст - данные, живущие между действиями
    context = {
        "arr1": None,
        "arr2": None,
        "result": None
    }

    # обработчики действий
    def _input_manual():
        try:
            arr1 = list(map(int, input("Массив 1 (через пробел): ").split()))
            arr2 = list(map(int, input("Массив 2 (через пробел): ").split()))
            if len(arr1) != len(arr2):
                raise ArraysLengthMismatchError(Messages.TASK1_ARRAYS_LEN_MISMATCH)
            context["arr1"] = arr1
            context["arr2"] = arr2
            context["result"] = None
            print(Messages.DATA_ENTERED)
        except Exception as e:
            print(f"Ошибка: {e}")

    def _input_random():
        try:
            n = int(input("Размер массивов: "))
            if n <= 0:
                raise InvalidInputError(Messages.INVALID_INPUT_SIZE)
            context["arr1"] = [random.randint(1, 20) for _ in range(n)]
            context["arr2"] = [random.randint(1, 20) for _ in range(n)]
            context["result"] = None
            print(Messages.GENERATED)
            print("Массив 1:", context["arr1"])
            print("Массив 2:", context["arr2"])
        except Exception as e:
            print(f"Ошибка: {e}")

    def _execute():
        if context["arr1"] is None or context["arr2"] is None:
            print(Messages.NO_DATA)
        else:
            try:
                context["result"] = solve(context["arr1"], context["arr2"])
                print(Messages.ALGO_DONE)
            except Exception as e:
                print(f"Ошибка: {e}")

    def _show_result():
        if context["result"] is None:
            print(Messages.NOT_EXECUTED)
        else:
            print(Messages.TASK1_RESULT, context["result"])
            input("\nНажмите Enter для возврата в меню...")

    # словарь автомата
    state_actions = {
        "1": _input_manual,
        "2": _input_random,
        "3": _execute,
        "4": _show_result,
        "5": None  # выход
    }

    # основной цикл автомата
    while True:
        print("\n--- Задание 1 ---")
        print("1. Ввести массивы вручную")
        print("2. Сгенерировать случайно")
        print("3. Выполнить алгоритм")
        print("4. Вывести результат")
        print("5. Назад в главное меню")
        choice = input("Выберите действие: ").strip()

        if choice not in state_actions:
            print(Messages.INVALID_CHOICE)
            continue

        if choice == "5":
            break

        state_actions[choice]()