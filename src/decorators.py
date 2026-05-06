# import datetime
import sys
from functools import wraps
from pathlib import Path
# from time import time
from typing import Any, Callable


def log(filename: str = None):
    """Декоратор для логирования выполнения функции"""

    def my_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def logging_wrapper(*args: Any, **kwargs: Any) -> Any:
            """Обертка для функции которая выполняет логирование"""

            result = None
            if filename is None:
                try:
                    # start_time = time()
                    result = func(*args, **kwargs)
                    # end_time = time()
                    # print(f"{datetime.datetime.now()} Выполняется функция {func.__name__}")
                    print(f"{func.__name__} ok")
                    # print(f"Функция {func.__name__} выполнена за {end_time - start_time} секунд")
                    print(result)

                except Exception as e:
                    print(f"{func.__name__} error:{type(e).__name__} message: {e}", file=sys.stderr)
            else:
                project_root = Path("C:/Users/kirill/Desktop/python_learing/projects/my_proj")
                path_file = project_root / filename
                try:
                    # start_time = time()
                    result = func(*args, **kwargs)
                    # end_time = time()

                    with open(path_file, "w", encoding="utf-8") as file:
                        # file.write(f"{datetime.datetime.now()} Выполняется функция {func.__name__}\n")
                        file.write(f"{func.__name__} ok\n")
                        # file.write(f"Функция {func.__name__} выполнена за {end_time - start_time} секунд\n")
                        file.write(f"Результат: {result}\n")
                except Exception as e:
                    with open(path_file, "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error:{type(e).__name__} message: {e}")

            return result

        return logging_wrapper

    return my_decorator
