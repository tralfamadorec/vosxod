"""
точка входа в консольное приложение
программа объединяет три задания (1, 5, 8) в едином текстовом интерфейсе
пользователь выбирает задание через главное меню, после чего запускается
соответствующее подменю с полной функциональностью:
- ввод данных (вручную или случайно),
- выполнение алгоритма,
- вывод результата.

соблюдены все требования:
- алгоритм недоступен без данных
- результат недоступен без выполнения
- при новых данных результат сбрасывается

модули:
    tasks.task1 — Задание 1: обработка двух массивов с сортировкой и обнулением совпадений
    tasks.task5 — Задание 5: подсчёт подмассивов с заданной суммой
    tasks.task8 — Задание 8: подсчёт общих чисел с учётом перевёрнутых версий
"""
import logging
from tasks import task1, task5, task8

# настройка логгера
logger = logging.getLogger("main")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("main.log", encoding="utf-8")
handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s"))

if not logger.handlers:
    logger.addHandler(handler)
    logger.propagate = False


def main():
    # главное меню программы как конечный автомат
    from errors import Messages

    # словарь переходов:
    menu_actions = {
        "1": lambda: task1.menu(),
        "2": lambda: task5.menu(),
        "3": lambda: task8.menu(),
        "4": None  # выход
    }

    logger.info("Запуск главного меню программы")

    while True:
        print("\n=== Главное меню ===")
        print("1. Задание 1")
        print("2. Задание 5")
        print("3. Задание 8")
        print("4. Выход")
        choice = input("Выберите задание: ").strip()
        logger.info(f"Пользователь выбрал в главном меню: {choice}")

        if choice not in menu_actions:
            print(Messages.INVALID_CHOICE)
            logger.info("Неверный выбор в главном меню")
            continue

        if choice == "4":
            print("Программа завершена.")
            logger.info("Программа завершена пользователем")
            break

        # выполняем выбранное задание
        menu_actions[choice]()
        # после возврата - остаёмся в главном меню (петля автомата)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")
        logger.info("Программа прервана пользователем (Ctrl+C)")
    except Exception as e:
        print(f"Критическая ошибка: {e}")
        logger.critical(f"Критическая ошибка в главном потоке: {e}")