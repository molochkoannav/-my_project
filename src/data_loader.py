import logging
from pathlib import Path

import pandas as pd

current_file = Path(__file__)
project_root = current_file.parent.parent
log_dir = project_root / "logs"
log_dir.mkdir(exist_ok=True)

log_file_dl = log_dir / "data_loader.log"

logging.getLogger("urllib3").setLevel(logging.WARNING)
logger_dl = logging.getLogger("data_loader")
logger_dl.setLevel(logging.DEBUG)

file_handler_dl = logging.FileHandler(log_file_dl, mode="w", encoding="utf-8")
file_handler_dl.setLevel(logging.DEBUG)


formatter = logging.Formatter("%(asctime)s - %(funcName)s - %(levelname)s: %(message)s")
file_handler_dl.setFormatter(formatter)


logger_dl.addHandler(file_handler_dl)
logger_dl.propagate = False


def csv_reader(file_path: Path) -> list[dict]:
    """Функция читает файл csv и возвращает список словарей"""

    try:
        logger_dl.info(f"Файл {file_path} найден, начинаем читать")
        df_csv = pd.read_csv(file_path, delimiter=";", encoding="utf-8")
        df_csv.set_index("id", inplace=True)
        list_transaction_csv = df_csv.to_dict(orient="records")
        logger_dl.info(f"Успешно прочитано {len(list_transaction_csv)} записей")
        return list_transaction_csv

    except FileNotFoundError:
        logger_dl.error(f"Файл {file_path} не найден")
        raise
    except pd.errors.EmptyDataError:
        logger_dl.error(f"Файл {file_path} пуст")
        raise
    except Exception as e:
        logger_dl.error(f"Ошибка при чтении файла {file_path}: {e}")
        raise


def excel_reader(file_path: Path) -> list[dict]:
    """Функция читает файл excel и возвращает список словарей"""
    try:
        logger_dl.info(f"Файл {file_path} найден, начинаем читать")
        df_excel = pd.read_excel(file_path)
        df_excel.set_index("id", inplace=True)
        list_transaction_excel = df_excel.to_dict(orient="records")
        logger_dl.info(f"Успешно прочитано {len(list_transaction_excel)} записей")
        return list_transaction_excel
    except FileNotFoundError:
        logger_dl.error(f"Файл {file_path} не найден")
        raise
    except pd.errors.EmptyDataError:
        logger_dl.error(f"Файл {file_path} пуст")
        raise
    except Exception as e:
        logger_dl.error(f"Ошибка при чтении файла {file_path}: {e}")
        raise
