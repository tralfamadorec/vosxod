import socket
import json
import time
import random
import logging
from datetime import datetime

# импортируем чистые функции из tasks
from tasks.task1 import solve as task1_solve
from tasks.task5 import count_subarrays_with_sum
from tasks.task8 import count_common_with_reverse

# логирование в файл
logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%H:%M:%S"
)

HOST = "127.0.0.1"
PORT = 65432

def handle_client(client_socket, client_id):
    try:
        data = client_socket.recv(4096).decode()
        request = json.loads(data)
        task = request.get("task")

        # эмуляция долгого расчёта (один раз на запрос)
        time.sleep(random.uniform(0.5, 2.0))

        if task == "task1":
            arr1 = request["arr1"]
            arr2 = request["arr2"]
            result = task1_solve(arr1, arr2)
            logging.info(f"Клиент{client_id}: выполнено задание 1")
            response = {"status": "ok", "result": result}

        elif task == "task5":
            arr = request["arr"]
            target = request["target"]
            result = count_subarrays_with_sum(arr, target)
            logging.info(f"Клиент{client_id}: выполнено задание 5")
            response = {"status": "ok", "result": result}

        elif task == "task8":
            arr1 = request["arr1"]
            arr2 = request["arr2"]
            result = count_common_with_reverse(arr1, arr2)
            logging.info(f"Клиент{client_id}: выполнено задание 8")
            response = {"status": "ok", "result": result}

        else:
            response = {"status": "error", "message": "Неизвестное задание"}

        client_socket.send(json.dumps(response).encode())

    except Exception as e:
        error_msg = f"Клиент{client_id}: ошибка — {e}"
        logging.error(error_msg)
        client_socket.send(
            json.dumps({"status": "error", "message": str(e)}).encode()
        )
    finally:
        client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Сервер запущен на {HOST}:{PORT}")

    client_id = 1
    try:
        while True:
            client_socket, addr = server.accept()
            print(f"Подключился клиент {client_id} ({addr})")
            handle_client(client_socket, client_id)
            client_id += 1
    except KeyboardInterrupt:
        print("\nСервер остановлен")
    finally:
        server.close()

if __name__ == "__main__":
    main()