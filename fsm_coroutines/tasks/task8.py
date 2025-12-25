from errors import EmptyArrayError, InvalidInputError, NegativeNumberError, Messages
import random

# чистая логика

def reverse_number(n):
    # возвращает перевёрнутое число без лидирующих нулей
    if n < 0:
        raise NegativeNumberError(Messages.TASK8_NEGATIVE_NUMBER)
    return int(str(n)[::-1])

def count_common_with_reverse(arr1, arr2):
    # считает, сколько элементов из arr1 встречаются в arr2 или их перевёрнутых версиях
    if not arr1 or not arr2:
        raise EmptyArrayError(Messages.TASK8_EMPTY_ARRAY)
    count = 0
    for x in arr1:
        if x in arr2 or reverse_number(x) in arr2:
            count += 1
    return count


# FSM через корутины (одно состояние — menu)

class Task8FSM:
    def __init__(self):
        self.arr1 = None
        self.arr2 = None
        self.result = None
        self.menu_state = self._create_menu()
        next(self.menu_state)  # заправка

    def _create_menu(self):
        while True:
            event = yield
            choice = event.get("choice")

            if choice == "1":
                try:
                    arr1 = list(map(int, event["arr1"].split()))
                    arr2 = list(map(int, event["arr2"].split()))
                    if not arr1 or not arr2:
                        raise EmptyArrayError(Messages.TASK8_EMPTY_ARRAY)
                    if any(x < 0 for x in arr1 + arr2):
                        raise NegativeNumberError(Messages.TASK8_NEGATIVE_NUMBER)
                    self.arr1, self.arr2 = arr1, arr2
                    self.result = None
                    print(Messages.DATA_ENTERED)
                except Exception as err:
                    print(f"Ошибка: {err}")

            elif choice == "2":
                try:
                    n = int(event["n"])
                    if n <= 0:
                        raise InvalidInputError(Messages.INVALID_INPUT_SIZE)
                    # генерируем ТОЛЬКО положительные числа (для корректного reverse)
                    self.arr1 = [random.randint(10, 999) for _ in range(n)]
                    self.arr2 = [random.randint(10, 999) for _ in range(n)]
                    self.result = None
                    print(Messages.GENERATED)
                    print("Массив 1:", self.arr1)
                    print("Массив 2:", self.arr2)
                except Exception as err:
                    print(f"Ошибка: {err}")

            elif choice == "3":
                if self.arr1 is None or self.arr2 is None:
                    print(Messages.NO_DATA)
                else:
                    try:
                        self.result = count_common_with_reverse(self.arr1, self.arr2)
                        print(Messages.ALGO_DONE)
                    except Exception as err:
                        print(f"Ошибка: {err}")

            elif choice == "4":
                if self.result is None:
                    print(Messages.NOT_EXECUTED)
                else:
                    print(f"{Messages.TASK8_RESULT_PREFIX} {self.result}")
                    input("\nНажмите Enter для возврата в меню...")

            elif choice == "5":
                return

            else:
                print(Messages.INVALID_CHOICE)

    def send(self, event):
        try:
            self.menu_state.send(event)
            return True
        except StopIteration:
            return False

    def run(self):
        print("\n--- Задание 8 (FSM через корутины) ---")
        while True:
            print("\n1. Ввести массивы вручную")
            print("2. Сгенерировать случайно")
            print("3. Выполнить алгоритм")
            print("4. Вывести результат")
            print("5. Назад")
            choice = input("Выбор: ").strip()

            if choice == "1":
                arr1 = input("Массив 1: ")
                arr2 = input("Массив 2: ")
                if not self.send({"choice": choice, "arr1": arr1, "arr2": arr2}):
                    break
            elif choice == "2":
                n = input("Размер массивов: ")
                if not self.send({"choice": choice, "n": n}):
                    break
            elif choice == "3":
                if not self.send({"choice": choice}):
                    break
            elif choice == "4":
                if not self.send({"choice": choice}):
                    break
            elif choice == "5":
                self.send({"choice": choice})
                break
            else:
                self.send({"choice": choice})


if __name__ == "__main__":
    print("🔍 Тестирование чистой логики задания 8 (count_common_with_reverse):")
    print("-" * 75)

    try:
        arr1 = [12, 34, 56]
        arr2 = [21, 78, 65]
        result = count_common_with_reverse(arr1, arr2)
        expected = 2  # 12 ↔ 21, 56 ↔ 65
        print(f"{arr1} и {arr2} → {result}")
        assert result == expected
    except Exception as err:
        print(f"Ошибка: {err}")

    try:
        count_common_with_reverse([-5], [5])
        print("Ошибка не возникла")
    except NegativeNumberError as err:
        print(f"Ожидаемая ошибка: {err}")

    try:
        count_common_with_reverse([], [1])
        print("Ошибка не возникла")
    except EmptyArrayError as err:
        print(f"Ожидаемая ошибка: {err}")

    print("\nТест задания 8 завершён.")