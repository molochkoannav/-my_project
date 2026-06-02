from src.utils import get_read_transactions
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.utils import process_bank_search
import pandas as pd


# def get_valid_state()-> str | None:
#     """Запрашивает статус пока пользователь не введет корректный"""
#     valid_states = {"EXECUTED", "CANCELED", "PENDING"}
#     i = 0
#     while i < 3:
#         print("\nДоступные статусы: EXECUTED, CANCELED, PENDING")
#         state = input("Введите статус: ").upper()
#         if state in valid_states:
#             return state
#         else:
#             i += 1
#             print(f"Статус операции '{state}' недоступен.")
#             print("Введите статус, по которому необходимо выполнить фильтрацию.")
#             print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
#
#
# def handle_sorting(transactions: list[dict]) -> list[dict]:
#     """Обрабатывает сортировку транзакций по желанию пользователя"""
#     user_confirmation = input("Отсортировать операции по дате? (Да/Нет): ")
#     user_confirmation_reverse = input("Отсортировать по возрастанию/ по убыванию? ")
#     if user_confirmation.lower() == "да" and user_confirmation_reverse.lower() == "по убыванию":
#         return sort_by_date(transactions, reverse=True)
#     elif user_confirmation.lower() == "да" and user_confirmation_reverse.lower() == "по возрастанию":
#         return sort_by_date(transactions, reverse=False)
#     return transactions
#
# def get_filtered_valute_transactions(transactions: list[dict]) -> list[dict]:
#     """Фильтрует транзакции по типу"""
#     user_confirmation = input("Выводить только рублевые транзакции? Да/Нет ").lower()
#     if user_confirmation == "да":
#         filtered_transactions = [
#             item
#             for item in transactions
#             if isinstance(item, dict) and item.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
#         ]
#     else:
#         filtered_transactions = transactions
#
#     return filtered_transactions
#
#
# def handle_json():
#     """Обработка JSON файла"""
#     print("Для обработки выбран JSON-файл")
#     transactions = get_read_transactions("data/operations.json")
#
#     state = get_valid_state()
#     print(f"Операции отфильтрованы по статусу '{state}'")
#
#     filtered_operations = filter_by_state(transactions, state)
#     sorted_operations = handle_sorting(filtered_operations)
#     filtered_transactions_valute = get_filtered_valute_transactions(sorted_operations)
#     user_search = input(f"Отфильтровать список транзакций по определенному слову в описании? Да/Нет ").lower()
#     if user_search == "да":
#         looking_for_words = input("Введите слово или фразу для поиска: ").lower()
#         searching_description = process_bank_search(filtered_transactions_valute, looking_for_words)
#         return searching_description
#     else:
#         return filtered_transactions_valute
#
#

def main():
    while True:
        print("\nПривет! Добро пожаловать в программу работы с банковскими транзакциями")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        user_input = input("Введите номер пункта меню: ")

        if user_input == "1":
            print("Для обработки выбран JSON-файл")
            transactions = get_read_transactions("data/operations.json")
            new_json = []
            for transaction in transactions:
                new_json.append({"id":transaction.get("id"),
                                "state":transaction.get("state"),
                                "date":transaction.get("date"),
                                "amount":transaction.get("operationAmount",{}).get("amount"),
                                "currency_name":transaction.get("operationAmount",{}).get("currency",{}).get("name"),
                                "currency_code": transaction.get("operationAmount",{}).get("currency",{}).get("code"),
                                "from": transaction.get("from"),
                                "to": transaction.get("to"),
                                "description": transaction.get("description")})
            print(*new_json,sep="\n")




            # if result != {}:
            #     print(f"\nВсего банковских транзакций:{len(result)} \n")
            #     print("Распечатываю итоговый список транзакций...")
            #     for transaction in result:
            #         print(transaction)
            # else:
            #     print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")




        elif user_input == "2":
            print("Для обработки выбран CSV-файл")
            # TODO: Получить информацию о транзакциях из CSV-файла
        elif user_input == "3":
            print("Для обработки выбран XLSX-файл")
             # TODO: Получить информацию о транзакциях из XLSX-файла
        else:
            print("Неверный выбор пункта меню. Попробуйте еще раз.")
        break


if __name__ == "__main__":
   main()
