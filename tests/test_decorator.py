import pytest
from src.decorators import log

def test_log(capsys):
    @log()
    def my_function(x, y):
        return x + y
    my_function(1, 2)
    out,err = capsys.readouterr()
    assert out == "my_function ok\n3\n"

    @log()
    def my_function(x, y):
        return x + y

    my_function(1, "2")
    out, err = capsys.readouterr()
    assert err == "my_function error:TypeError message: unsupported operand type(s) for +: 'int' and 'str'\n"

