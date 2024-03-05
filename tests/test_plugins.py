from app.plugins.square import SquareCommand
from app.plugins.mod import ModCommand

def test_square():
    command = SquareCommand(3)
    assert command.execute() == 9

def test_square_negative():
    command = SquareCommand(-4)
    assert command.execute() == 16

def test_modulus():
    command = ModCommand(10, 3)
    assert command.execute() == 1

def test_modulus_negative():
    command = ModCommand(-10, 3)
    assert command.execute() == 2

def test_modulus_by_one():
    command = ModCommand(5, 1)
    assert command.execute() == 0
