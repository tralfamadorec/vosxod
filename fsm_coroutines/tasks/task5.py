from errors import InvalidInputError, EmptyArrayError, Messages
import random

# чистая логика

def count_subarrays_with_sum(arr, target):
    # считает количество непрерывных подмассивов с суммой, равной target
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
    return count


# FSM через корутины (одно состояние — menu)

class Task5FSM:
    def __init__(self):
        self.arr = None
        self.target = None
        self.result = None
        self.menu_state = self._create_menu()
        next(self.menu_state)  # заправка

    def _create_menu(self):
        while True:
            event = yield
            choice = event.get("choice")

            if choice == "1":
                try:
                    arr = list(map(int, event["arr"].split()))
                    target = int(event["target"])
                    if not arr:
                        raise EmptyArrayError(Messages.TASK5_EMPTY_ARRAY)
                    self.arr, self.target = arr, target
                    self.result = None
                    print(Messages.DATA_ENTERED)
                except Exception as err:
                    print(f"Ошибка: {err}")

            elif choice == "2":
                try:
                    n = int(event["n"])
                    if n <= 0:
                        raise InvalidInputError(Messages.INVALID_INPUT_SIZE)
                    self.arr = [random.randint(-10, 10) for _ in range(n)]
                    self.target = random.randint(-5, 10)
                    self.result = None
                    print(Messages.GENERATED)
                    print("Массив:", self.arr)
                    print("Цель:", self.target)
                except Exception as err:
                    print(f"Ошибка: {err}")

            elif choice == "3":
                if self.arr is None or self.target is None:
                    print(Messages.NO_DATA)
                else:
                    try:
                        self.result = count_subarrays_with_sum(self.arr, self.target)
                        print(Messages.ALGO_DONE)
                    except Exception as err:
                        print(f"Ошибка: {err}")

            elif choice == "4":
                if self.result is None:
                    print(Messages.NOT_EXECUTED)
                else:
                    print(f"{Messages.TASK5_RESULT_PREFIX} {self.target}: {self.result}")
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
        print("\n--- Задание 5 (FSM через корутины) ---")
        while True:
            print("\n1. Ввести массив и цель вручную")
            print("2. Сгенерировать случайно")
            print("3. Выполнить алгоритм")
            print("4. Вывести результат")
            print("5. Назад")
            choice = input("Выбор: ").strip()

            if choice == "1":
                arr = input("Массив (через пробел): ")
                target = input("Целевое число: ")
                if not self.send({"choice": choice, "arr": arr, "target": target}):
                    break
            elif choice == "2":
                n = input("Размер массива: ")
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
    print("🔍 Тестирование чистой логики задания 5 (count_subarrays_with_sum):")
    print("-" * 70)

    try:
        arr = [1, 1, 1]
        target = 2
        result = count_subarrays_with_sum(arr, target)
        expected = 2
        print(f"Массив {arr}, сумма={target} → {result}")
        assert result == expected
    except Exception as err:
        print(f"Ошибка: {err}")

    try:
        count_subarrays_with_sum([], 5)
        print("Ошибка не возникла")
    except EmptyArrayError as err:
        print(f"Ожидаемая ошибка: {err}")

    print("\nТест задания 5 завершён.")