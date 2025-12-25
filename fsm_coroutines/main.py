"""
программа для запуска заданий 1, 5 и 8 в виде конечных автоматов,
реализованных через корутины
"""

from tasks.task1 import Task1FSM
from tasks.task5 import Task5FSM
from tasks.task8 import Task8FSM


def main():
    while True:
        print("\n" + "=" * 50)
        print("=== Главное меню (FSM через корутины) ===")
        print("1. Задание 1 - Обработка двух массивов")
        print("2. Задание 5 - Подмассивы с заданной суммой")
        print("3. Задание 8 - Общие числа с перевёрнутыми")
        print("4. Выход")
        print("=" * 50)
        choice = input("Выберите задание: ").strip()

        match choice:
            case "1":
                fsm = Task1FSM()
                fsm.run()
            case "2":
                fsm = Task5FSM()
                fsm.run()
            case "3":
                fsm = Task8FSM()
                fsm.run()
            case "4":
                print("Завершение работы программы.")
                break
            case _:
                print("Неверный выбор. Пожалуйста, введите 1, 2, 3 или 4.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
    except Exception as err:
        print(f"\nКритическая ошибка: {err}")