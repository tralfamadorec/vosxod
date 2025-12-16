from tasks import task1, task5, task8

def main():
    while True:
        print("\n=== ГЛАВНОЕ МЕНЮ ===")
        print("1. Задание 1")
        print("2. Задание 5")
        print("3. Задание 8")
        print("4. Выход")
        choice = input("Выберите задание: ").strip()

        if choice == "1":
            task1.menu()
        elif choice == "2":
            task5.menu()
        elif choice == "3":
            task8.menu()
        elif choice == "4":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()