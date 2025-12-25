# fsm_coroutines/tasks/task1.py

from errors import InvalidInputError, ArraysLengthMismatchError, Messages
import random

# чистая логика

def sort_desc(arr):
    return sorted(arr, reverse=True)

def sort_asc(arr):
    return sorted(arr)

def sum_arrays_with_zero(a, b):
    return [0 if x == y else x + y for x, y in zip(a, b)]

def solve(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ArraysLengthMismatchError(Messages.TASK1_ARRAYS_LEN_MISMATCH)
    a_sorted = sort_desc(arr1)
    b_sorted = sort_asc(arr2)
    summed = sum_arrays_with_zero(a_sorted, b_sorted)
    return sort_asc(summed)


# FSM через корутины (одно состояние — menu)
# FSM может иметь одно состояние, если логика меню линейна

class Task1FSM:
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
                    if len(arr1) != len(arr2):
                        raise ArraysLengthMismatchError(Messages.TASK1_ARRAYS_LEN_MISMATCH)
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
                    self.arr1 = [random.randint(1, 20) for _ in range(n)]
                    self.arr2 = [random.randint(1, 20) for _ in range(n)]
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
                        self.result = solve(self.arr1, self.arr2)
                        print(Messages.ALGO_DONE)
                    except Exception as err:
                        print(f"Ошибка: {err}")

            elif choice == "4":
                if self.result is None:
                    print(Messages.NOT_EXECUTED)
                else:
                    print(Messages.TASK1_RESULT, self.result)
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
        print("\n--- Задание 1 (FSM через корутины) ---")
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
    print("🔍 Тестирование чистой логики задания 1 (solve):")
    print("-" * 60)

    try:
        result = solve([5, 7, 4], [4, 9, 3])
        expected = [7, 8, 16]
        print(f"Успешно: [5,7,4] + [4,9,3] → {result}")
        assert result == expected
    except Exception as err:
        print(f"Ошибка: {err}")

    try:
        solve([1, 2], [1, 2, 3])
        print("Ошибка не возникла")
    except ArraysLengthMismatchError as err:
        print(f"Ожидаемая ошибка: {err}")

    print("\nТест завершён.")