from pathlib import Path

from src.decorators import log


def test_log(capsys) -> None:
    """Фикстура проверяет работу декоратора через сapsys при выводе в консоль"""

    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    out, err = capsys.readouterr()
    assert out == "my_function ok\n3\n"

    @log()
    def my_function(x, y):
        return x + y

    my_function(1, "2")
    out, err = capsys.readouterr()
    assert err == "my_function error:TypeError message: unsupported operand type(s) for +: 'int' and 'str'\n"


def test_log_filename():
    """Фикстура проверяет работу декоратора при записи в файл"""
    log_file = "mylog.txt"

    @log(filename=log_file)
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    project_root = Path("C:/Users/kirill/Desktop/python_learing/projects/my_proj")
    path_file = project_root / log_file
    with open(path_file, encoding="utf-8") as f:
        assert f.read() == "my_function ok\nРезультат: 3\n"

    @log(filename=log_file)
    def my_function(x, y):
        return x + y

    my_function(1, "2")
    project_root = Path("C:/Users/kirill/Desktop/python_learing/projects/my_proj")
    path_file = project_root / log_file
    with open(path_file, encoding="utf-8") as f:
        assert f.read() == "my_function error:TypeError message: unsupported operand type(s) for +: 'int' and 'str'"
