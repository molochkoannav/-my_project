from src.generators import filter_by_currency
from src.utils import get_read_transactions
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.utils import process_bank_search
from src.data_loader import csv_reader
from src.data_loader import excel_reader
from src.wiget import mask_account_card, get_date

def main() -> None:
    """
        Главная функция программы для работы с банковскими транзакциями.

        Позволяет пользователю:
        1. Выбрать источник данных (JSON, CSV или XLSX файл)
        2. Отфильтровать транзакции по статусу (EXECUTED, CANCELED, PENDING)
        3. Отсортировать по дате (по возрастанию/убыванию)
        4. Отфильтровать только рублевые транзакции
        5. Выполнить поиск по описанию транзакций

        Функция только выводит результаты в консоль
    """
    print("\nПривет! Добро пожаловать в программу работы с банковскими транзакциями")
    while True:
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        user_input = input("Введите номер пункта меню: ")
        data_choice_user = None
        if user_input == "1":
            print("Для обработки выбран JSON-файл")
            json_transactions = get_read_transactions("data/operations.json")
            new_json = []
            for transaction in json_transactions:
                new_json.append({"id":transaction.get("id"),
                                "state":transaction.get("state"),
                                "date":transaction.get("date"),
                                "amount":transaction.get("operationAmount",{}).get("amount"),
                                "currency_name":transaction.get("operationAmount",{}).get("currency",{}).get("name"),
                                "currency_code": transaction.get("operationAmount",{}).get("currency",{}).get("code"),
                                "from": transaction.get("from"),
                                "to": transaction.get("to"),
                                "description": transaction.get("description")})
            data_choice_user = new_json
            break

        elif user_input == "2":
            print("Для обработки выбран CSV-файл")
            csv_transaction = csv_reader("data/transactions.csv")
            data_choice_user = csv_transaction
            break

        elif user_input == "3":
            print("Для обработки выбран XLSX-файл")
            xlsx_transaction = excel_reader("data/transactions_excel.xlsx")
            data_choice_user = xlsx_transaction
            break
        else:
            print("Неверный выбор пункта меню. Попробуйте еще раз.")
    print("Программа: Введите статус, по которому необходимо выполнить фильтрацию.")
    while True:
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        state = input("Введите статус: ").upper()
        if state in ["EXECUTED", "CANCELED", "PENDING"]:
            filtered_operations = filter_by_state(data_choice_user, state)
            print(f"Операции отфильтрованы по статусу '{state}'")
            break
        else:
            print(f"Программа: Статус операции {state} недоступен.")


    while True:
        user_input = input("Отсортировать операции по дате? (Да/Нет) ").lower()
        if user_input == "да":
            user_confirmation_reverse = input("Отсортировать по возрастанию/ по убыванию? ")
            if user_confirmation_reverse == "по убыванию":
                filtered_operations = sort_by_date(filtered_operations)
                break
            elif user_confirmation_reverse == "по возрастанию":
                filtered_operations = sort_by_date(filtered_operations, reverse=False)
                break
            else:
                print("Неверный выбор. Попробуйте еще раз.")
                continue
        break
    user_input = input("Выводить только рублевые транзакции? Да/Нет ").lower()
    if user_input == "да":
        filtered_operations = filter_by_currency(filtered_operations, "RUB")
    user_input = input(f"Отфильтровать список транзакций по определенному слову в описании? Да/Нет ").lower()
    if user_input == "да":
         looking_for_words = input("Введите слово или фразу для поиска: ").lower()
         filtered_operations = process_bank_search(filtered_operations, looking_for_words)
    if filtered_operations == []:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print()
        print("Распечатываю итоговый список транзакций...")
        print()
        print(f"Всего банковских операций в выборке: {len(filtered_operations)}")

        for transaction in filtered_operations:
            date_transaction = get_date(transaction["date"])
            print(f"{date_transaction} {transaction.get('description')}")
            number_to = mask_account_card(transaction.get("to"))
            if transaction["from"] == "":
                print(number_to)
            else:
                number_from = mask_account_card(transaction.get("from"))
                print(f"{number_from} -> {number_to}")
            print(f"Сумма: {transaction.get('amount')} {transaction.get('currency_code')}")
            print()

if __name__ == "__main__":
   main()
