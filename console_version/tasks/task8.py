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
    # меню задания 8, реализованное через конечный автомат (FSM) с использованием словаря
    from errors import InvalidInputError, EmptyArrayError, NegativeNumberError, Messages
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
            if not arr1 or not arr2:
                raise EmptyArrayError(Messages.TASK8_EMPTY_ARRAY)
            if any(x < 0 for x in arr1 + arr2):
                raise NegativeNumberError(Messages.TASK8_NEGATIVE_NUMBER)
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
            # Генерируем только положительные числа (для корректного переворота)
            context["arr1"] = [random.randint(10, 999) for _ in range(n)]
            context["arr2"] = [random.randint(10, 999) for _ in range(n)]
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
                context["result"] = count_common_with_reverse(context["arr1"], context["arr2"])
                print(Messages.ALGO_DONE)
            except Exception as e:
                print(f"Ошибка: {e}")

    def _show_result():
        if context["result"] is None:
            print(Messages.NOT_EXECUTED)
        else:
            print(f"{Messages.TASK8_RESULT_PREFIX} {context['result']}")
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
        print("\n--- Задание 8 ---")
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


if __name__ == "__main__":
    print("Тестирование задания 8 (count_common_with_reverse):")
    print("-" * 60)

    # успешный
    try:
        res = count_common_with_reverse([12, 34, 56], [21, 78, 65])
        print("[12,34,56] и [21,78,65] ->", res)
    except Exception as e:
        print("Ошибка:", e)

    # отрицательное число
    try:
        count_common_with_reverse([-5], [5])
        print("Ошибка не возникла")
    except NegativeNumberError as e:
        print("Поймана ожидаемая ошибка:", e)

    # пустой массив
    try:
        count_common_with_reverse([], [1])
        print("Ошибка не возникла")
    except EmptyArrayError as e:
        print("Поймана ожидаемая ошибка:", e)

    print("\nТест завершён.")