
from typing import Union
import logging
from pathlib import Path


current_file = Path(__file__)
project_root = current_file.parent.parent
log_dir = project_root / 'logs'
log_dir.mkdir(exist_ok=True)

log_file = log_dir / 'masks.log'

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(funcName)s - %(levelname)s: %(message)s',
    filemode='w',
    encoding='utf-8')
logger = logging.getLogger(__name__)
logging.getLogger("urllib3").setLevel(logging.WARNING)


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция маскирует номер карты пользователя"""
    logger.info('Запуск модуля маскировки')
    if len(card_number) == 16 and card_number.isdigit() and not card_number.startswith(("0", "00", "000", "0000")):
        list_card_number = [number for number in (str(card_number))]
        list_card_number[6:-4] = ["*", "*", "*", "*", "*", "*"]
        for num in range(len(list_card_number) // 4 - 1, 0, -1):
            list_card_number[num * 4: num * 4] = [" "]

        mask_card_number = "".join(list_card_number)
        logger.info('Маскировка номера карты выполнена')
        return mask_card_number

    else:
        logger.warning('Ошибка в наборе номера карты')
        return "Номер карты набран не верно"



def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция маскирует номер счета пользователя"""
    logger.info('Запуск модуля маскировки счета')
    if (
        len(account_number) == 20
        and account_number.isdigit()
        and not account_number.startswith(("0", "00", "000", "0000"))
    ):
        list_account_number = [number for number in (str(account_number))]
        list_account_number[:-4] = ["*", "*"]
        mask_account = "".join(list_account_number)
        logger.info('Маскировка номера счета выполнена')
        return mask_account
    else:
        logger.warning('Ошибка в наборе номера счета')
        return "Номер счета набран не верно"
