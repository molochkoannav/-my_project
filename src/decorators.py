from time import time
import datetime
from functools import wraps
from typing import Any
from pathlib import Path

def log(filename: [str] = None):
    """Декоратор для логирования выполнения функции"""
    def my_decorator(func):
        @wraps(func)
        def logging_wrapper(*args: Any, **kwargs: Any) -> Any:
            """Обертка для функции которая выполняет логирование"""

            result = None
            if filename is None:
                try:
                    start_time = time()
                    result = func(*args, **kwargs)
                    end_time = time()
                    print(f"{datetime.datetime.now()} Выполняется функция {func.__name__}")
                    print(f"{func.__name__} ok")
                    print(f"Функция {func.__name__} выполнена за {end_time - start_time} секунд")
                    print(result)

                except Exception as e:
                    print(f"{func.__name__} error:{type(e).__name__} message: {e}")
            else:
                project_root = Path("C:/Users/kirill/Desktop/python_learing/projects/my_proj")
                path_file = project_root / filename
                try:
                    start_time = time()
                    result = func(*args, **kwargs)
                    end_time = time()

                    with open(path_file, "a", encoding="utf-8") as file:
                        file.write(f"{datetime.datetime.now()} Выполняется функция {func.__name__}\n")
                        file.write(f"Функция {func.__name__} выполнена за {end_time - start_time} секунд\n")
                        file.write(f"Результат: {result}\n")
                except Exception as e:
                    with open(path_file, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error:{type(e).__name__} message: {e}")

            return result
        return logging_wrapper
    return my_decorator

