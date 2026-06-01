from src.utils import get_read_transactions
from src.processing import filter_by_state
from src.processing import sort_by_date


def main():
    while True:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        user_input = input("Введите номер пункта меню: ")
        if user_input == "1":
            print("Для обработки выбран JSON-файл")
            search_in_json = get_read_transactions("data/operations.json")
            print("Введите статус, по которому необходимо выполнить фильтрацию.")
            print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
            state = input("Введите статус: ")
            if state == "EXECUTED" or state == "CANCELED" or state == "PENDING":
                print(f"Операции отфильтрованы по статусу \'{state}\'")
                filtered_operations = filter_by_state(search_in_json, state)
                print("Отсортировать операции по дате? Да/Нет")
                user_confirmation = input("Введите ответ: ")
                if user_confirmation == "Да":
                    sorted_operations = sort_by_date(filtered_operations, reverse=True)

            else:
                print(f"Статус операции \'{state}\' недоступен.")
                print("Введите статус, по которому необходимо выполнить фильтрацию.")
                print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        elif user_input == "2":
            print("Для обработки выбран CSV-файл")
            # TODO: Получить информацию о транзакциях из CSV-файла
        elif user_input == "3":
            print("Для обработки выбран XLSX-файл")
             # TODO: Получить информацию о транзакциях из XLSX-файла
        else:
            print("Неверный выбор пункта меню. Попробуйте еще раз.")


if __name__ == "__main__":
   main()