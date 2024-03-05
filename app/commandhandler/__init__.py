from app.commands import Command
import inspect

from app.commands.menu import MenuCommand


class CommandHandler:
    def __init__(self):
        self.command = Command()
        self.command_list = {}
    

    def register_command(self, command_name: str, command_class: Command):
        self.command_list[command_name] = command_class


    def execute_command(self, command_name, *operands):
        if command_name == 'menu':
            # Correct instantiation of MenuCommand and calling its execute method
            command_instance = MenuCommand(list(self.get_keys()))
            return command_instance.execute()
        
        # Check if the command exists
        if command_name not in self.command_list:
            raise ValueError(f"Unsupported command: {command_name}")

        # Retrieve the command class and inspect its constructor
        command_class = self.command_list[command_name]
        constructor_params = inspect.signature(command_class.__init__).parameters

        # The number of expected operands is the constructor parameters minus 'self'
        expected_operand_count = len(constructor_params) - 1

        # Validate the number of provided operands against the expected count
        if len(operands) != expected_operand_count:
            raise ValueError(f"Expected {expected_operand_count} operands for '{command_name}' but got {len(operands)}.")

        # Instantiate and execute the command if the operand count is correct
        command_instance = command_class(*operands)
        return command_instance.execute()

    
    
    def get_keys(self):
        return self.command_list.keys()