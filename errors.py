# классы исключений
class TaskError(Exception):
    # базовое исключение для всех заданий
    pass

class InvalidInputError(TaskError):
    # ошибка некорректного пользовательского ввода
    pass

class ArraysLengthMismatchError(TaskError):
    # массивы разной длины (только задание 1)
    pass

class EmptyArrayError(TaskError):
    # массив пуст (задания 5, 8)
    pass

class NegativeNumberError(TaskError):
    # отрицательное число недопустимо (задание 8)
    pass


class Messages:
    # ОБЩИЕ СООБЩЕНИЯ (для всех заданий)
    INVALID_INPUT_INT = "Ошибка: введите только целые числа!"
    INVALID_INPUT_SIZE = "Размер должен быть больше нуля!"
    NO_DATA = "Ошибка: сначала введите данные!"
    NOT_EXECUTED = "Ошибка: сначала выполните алгоритм!"
    DATA_ENTERED = "Данные успешно введены."
    GENERATED = "Сгенерировано:"
    ALGO_DONE = "Алгоритм выполнен."
    INVALID_CHOICE = "Неверный выбор."
    EXIT = "Пользователь вышел из меню"

    # СПЕЦИФИЧНЫЕ СООБЩЕНИЯ
    # задание 1
    TASK1_ARRAYS_LEN_MISMATCH = "Массивы должны быть одинаковой длины"
    TASK1_RESULT = "Результат:"

    # задание 5
    TASK5_EMPTY_ARRAY = "Массив не должен быть пустым"
    TASK5_RESULT_PREFIX = "Количество подмассивов с суммой"

    # задание 8
    TASK8_EMPTY_ARRAY = "Массивы не должны быть пустыми"
    TASK8_NEGATIVE_NUMBER = "Числа должны быть положительными"
    TASK8_RESULT_PREFIX = "Общих чисел (с перевёрнутыми):"