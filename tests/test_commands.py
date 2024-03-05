import pytest
from app.operations.add import AddCommand
from app.operations.subtract import SubtractCommand
from app.operations.multiply import MultiplyCommand
from app.operations.divide import DivideCommand

def test_add_command():
    add_command = AddCommand(1, 2)
    assert add_command.execute() == 3

def test_subtract_command():
    subtract_command = SubtractCommand(5, 2)
    assert subtract_command.execute() == 3

def test_multiply_command():
    multiply_command = MultiplyCommand(3, 4)
    assert multiply_command.execute() == 12

def test_divide_command():
    divide_command = DivideCommand(8, 2)
    assert divide_command.execute() == 4

def test_divide_by_zero():
    divide_command = DivideCommand(8, 0)
    with pytest.raises(ZeroDivisionError):
        divide_command.execute()
