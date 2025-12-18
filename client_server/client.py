import socket
import json
from datetime import datetime

HOST = "127.0.0.1"
PORT = 65432

def log(msg):
    print(f"{datetime.now().strftime('%H:%M:%S')} {msg}")

def input_array(prompt):
    return list(map(int, input(prompt).split()))

def main():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
    except ConnectionRefusedError:
        log("Клиент: сервер не запущен!")
        return

    while True:
        print("\n--- Клиент ---")
        print("1. Задание 1: Обработка двух массивов")
        print("2. Задание 5: Подмассивы с заданной суммой")
        print("3. Задание 8: Общие числа с перевёрнутыми")
        print("4. Выйти")
        choice = input("Выберите задание: ").strip()

        request = None

        if choice == "1":
            arr1 = input_array("Массив 1 (через пробел): ")
            arr2 = input_array("Массив 2 (через пробел): ")
            request = {"task": "task1", "arr1": arr1, "arr2": arr2}
            log("Клиент: отправлен запрос на обработку задания 1")

        elif choice == "2":
            arr = input_array("Массив (через пробел): ")
            target = int(input("Целевое число: "))
            request = {"task": "task5", "arr": arr, "target": target}
            log("Клиент: отправлен запрос на обработку задания 5")

        elif choice == "3":
            arr1 = input_array("Массив 1 (через пробел): ")
            arr2 = input_array("Массив 2 (через пробел): ")
            request = {"task": "task8", "arr1": arr1, "arr2": arr2}
            log("Клиент: отправлен запрос на обработку задания 8")

        elif choice == "4":
            break

        else:
            print("Неверный выбор.")
            continue

        # Отправка
        sock.send(json.dumps(request).encode())

        # Получение ответа
        response = json.loads(sock.recv(4096).decode())
        if response["status"] == "ok":
            log(f"Клиент: получен результат: {response['result']}")
        else:
            log(f"Клиент: ошибка — {response['message']}")

    sock.close()
    log("Клиент: отключён")

if __name__ == "__main__":
    main()