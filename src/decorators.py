from time import time
import datetime
from typing import Callable
def log(func: Callable, file_name) -> Callable:
    pass
    # @wraps(func: Callable)-> Callable:
    # def wrapper(*args: Any, **kwargs: Any) -> Any:
    #     if func(file_name):
    #         with open (f'{func__name__}', 'a') as file:
    #