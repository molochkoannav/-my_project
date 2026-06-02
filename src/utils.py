import json
import logging
from collections import Counter
from pathlib import Path
import re


current_file = Path(__file__)
project_root = current_file.parent.parent
log_dir = project_root / "logs"
log_dir.mkdir(exist_ok=True)

log_file_ut = log_dir / "utils.log"

logging.getLogger("urllib3").setLevel(logging.WARNING)
logger_ut = logging.getLogger("utils")
logger_ut.setLevel(logging.DEBUG)


file_handler_ut = logging.FileHandler(log_file_ut, mode="w", encoding="utf-8")
file_handler_ut.setLevel(logging.DEBUG)


formatter = logging.Formatter("%(asctime)s - %(funcName)s - %(levelname)s: %(message)s")
file_handler_ut.setFormatter(formatter)


logger_ut.addHandler(file_handler_ut)
logger_ut.propagate = False


def get_read_transactions(file_path):
    """
    Принимает путь до JSON-файла
    и возвращает список словарей с
    данными о финансовых транзакциях"""
    logger_ut.info("Запуск модуля чтения данных")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger_ut.info("Данные считаны")
                return data
            else:
                logger_ut.warning("Данные не считаны")
                return []
    except FileNotFoundError:
        logger_ut.error("Файл не найден")
        return []
    except json.decoder.JSONDecodeError:
        logger_ut.error("Ошибка чтения данных")
        return []
    except ValueError:
        logger_ut.error("Ошибка чтения данных")
        return []


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""

    pattern = re.compile(f"{search}", re.IGNORECASE)
    searching_transactions = [transaction for transaction in data if pattern.search(transaction["description"])]
    return searching_transactions


def process_bank_operations(data:list[dict], categories:list)->dict:
    """Принимает список словарей с данными о банковских операциях и возвращает словарь,
    в котором ключами являются категории, а значениями - списки словарей с данными о транзакциях."""
    patterns = {
        "Платежи": re.compile(r"платеж|оплата", re.IGNORECASE),
        "Переводы": re.compile(r"перевод", re.IGNORECASE),
        "Вклады": re.compile(r"вклад|открытие вклада", re.IGNORECASE)
    }

    # Один проход: для каждой транзакции определяем категорию и сразу считаем
    category_list = [
        category
        for transaction in data
        if transaction.get("description")
        for category, pattern in patterns.items()
        if pattern.search(transaction["description"])
    ]

    counter = Counter(category_list)

    return {category: counter.get(category, 0) for category in categories}




