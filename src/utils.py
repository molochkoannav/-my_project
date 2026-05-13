import json

def get_read_transactions(file_path):
    """
       Принимает путь до JSON-файла
       и возвращает список словарей с
       данными о финансовых транзакциях"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []
    except ValueError:
        return []


