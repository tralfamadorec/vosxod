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
    # меню задания 5, реализованное через конечный автомат (FSM) с использованием словаря
    from errors import InvalidInputError, EmptyArrayError, Messages
    import random

    # контекст - данные, живущие между действиями
    context = {
        "arr": None,
        "target": None,
        "result": None
    }

    # обработчики действий
    def _input_manual():
        try:
            arr = list(map(int, input("Массив (через пробел): ").split()))
            target = int(input("Целевое число: "))
            if not arr:
                raise EmptyArrayError(Messages.TASK5_EMPTY_ARRAY)
            context["arr"] = arr
            context["target"] = target
            context["result"] = None
            print(Messages.DATA_ENTERED)
        except Exception as e:
            print(f"Ошибка: {e}")

    def _input_random():
        try:
            n = int(input("Размер массива: "))
            if n <= 0:
                raise InvalidInputError(Messages.INVALID_INPUT_SIZE)
            context["arr"] = [random.randint(-10, 10) for _ in range(n)]
            context["target"] = random.randint(-5, 10)
            context["result"] = None
            print(Messages.GENERATED)
            print("Массив:", context["arr"])
            print("Целевое число:", context["target"])
        except Exception as e:
            print(f"Ошибка: {e}")

    def _execute():
        if context["arr"] is None or context["target"] is None:
            print(Messages.NO_DATA)
        else:
            try:
                context["result"] = count_subarrays_with_sum(context["arr"], context["target"])
                print(Messages.ALGO_DONE)
            except Exception as e:
                print(f"Ошибка: {e}")

    def _show_result():
        if context["result"] is None:
            print(Messages.NOT_EXECUTED)
        else:
            print(f"{Messages.TASK5_RESULT_PREFIX} {context['target']}: {context['result']}")
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
        print("\n--- Задание 5 ---")
        print("1. Ввести массив и число вручную")
        print("2. Сгенерировать данные случайно")
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