import pytest
from app.operations.add import AddCommand
from app.operations.subtract import SubtractCommand
from app.operations.multiply import MultiplyCommand
from app.operations.divide import DivideCommand
from app.commandhandler import CommandHandler
from app import App
from app.utility.MockInputOutput import MockInputOutput

def test_command_registration():
    handler = CommandHandler()
    handler.register_command('add', AddCommand)
    assert 'add' in handler.get_keys()

def test_command_registration_and_execution():
    handler = CommandHandler()
    handler.register_command('add', AddCommand)
    handler.register_command('subtract', SubtractCommand)
    handler.register_command('multiply', MultiplyCommand)
    handler.register_command('divide', DivideCommand)

    assert handler.execute_command('add', 1, 2) == 3
    assert handler.execute_command('subtract', 5, 2) == 3
    assert handler.execute_command('multiply', 3, 4) == 12
    assert handler.execute_command('divide', 8, 2) == 4

def test_invalid_command():
    handler = CommandHandler()
    with pytest.raises(ValueError):
        handler.execute_command('nonexistent', 1, 2)

def test_large_number_addition():
    add_command = AddCommand(1e308, 1e308)
    assert add_command.execute() == float('inf')

def test_subtraction_with_negative_result():
    subtract_command = SubtractCommand(5, 10)
    assert subtract_command.execute() == -5

def test_sequence_of_operations():
    with MockInputOutput(inputs=['add 1 2', 'add 5 3', 'subtract 3 2', 'multiply 5 6', 'exit']) as mock_io:
        app = App()
        app.command_handler.register_command('add', AddCommand)
        app.command_handler.register_command('subtract', SubtractCommand)
        app.command_handler.register_command('multiply', MultiplyCommand)
        app.run()
        output = mock_io.get_output()
    
    assert 'Result: 3' in output
    assert 'Result: 8' in output