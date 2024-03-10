import importlib
import pkgutil
from app.commands import Command
from app.operations.add import AddCommand
from app.operations.divide import DivideCommand
from app.operations.multiply import MultiplyCommand
from app.operations.subtract import SubtractCommand
from app.commandhandler import CommandHandler
from dotenv import load_dotenv
import os
import logging 
import logging.config

class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.command_handler = CommandHandler()
        self.discover_and_load_plugins()
        self.register_commands()


    def configure_logging(self):
        logging_conf_path = "logging.conf"
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path)
        else:
            logging.basicConfig(level=logging.INFO, filename='logs/app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging Configured")


    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        # print(settings)
        print("Environment Variables:")
        for key, value in os.environ.items():
            print(f"{key}: {value}")
        logging.info("Environment variables loaded")
        return settings


    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)        


    def discover_and_load_plugins(self):
        plugin_path = "app.plugins"
        module_info = pkgutil.iter_modules(importlib.import_module(plugin_path).__path__)
        for _, name, _ in module_info:
            imported_module = importlib.import_module(f"{plugin_path}.{name}")
            for attribute_name in dir(imported_module):
                attribute = getattr(imported_module, attribute_name)
                try:
                    if issubclass(attribute, Command) and attribute is not Command:
                        # Remove 'Command' from the end of the class name if present
                        command_name = attribute.command_name if hasattr(attribute, 'command_name') else attribute_name
                        if command_name.endswith('Command'):
                            command_name = command_name[:-7].lower()
                        self.command_handler.register_command(command_name, attribute)
                except TypeError:
                    # This means that the attribute is not a class, ignore
                    continue


    def register_commands(self):
        self.command_handler.register_command('add', AddCommand)
        self.command_handler.register_command('subtract', SubtractCommand)
        self.command_handler.register_command('multiply', MultiplyCommand)
        self.command_handler.register_command('divide', DivideCommand)


    def get_user_input(self):
        return input("\nEnter command: ").strip().lower()


    def parse_input(self, input_str):
        parts = input_str.split()
        command = parts[0]

        # For the 'menu' command or any command not requiring operands
        if command == "menu" or len(parts) == 1:
            return command, []

        # Handle the case with one operand
        elif len(parts) == 2:
            try:
                operand = float(parts[1])
            except ValueError:
                raise ValueError("Invalid input format. Expected a numeric value for the operand.")
            return command, [operand]

        # Handle the case with two operands
        elif len(parts) == 3:
            try:
                operand1 = float(parts[1])
                operand2 = float(parts[2])
            except ValueError:
                raise ValueError("Invalid input format. Expected numeric values for operands.")
            return command, [operand1, operand2]

        else:
            raise ValueError("Invalid input format. Expected: command [operand1] [operand2]")


    

    def display_menu(self):
        self.command_handler.execute_command("menu", None, None)


    def run(self):
        self.display_menu()
        while True:
            user_input = self.get_user_input()
            if user_input == 'exit':
                print("Exiting App")
                break

            try:
                command, operands = self.parse_input(user_input)
                if command == 'menu':
                    self.display_menu()
                else:
                    operands = list(map(float, operands))
                    result = self.command_handler.execute_command(command, *operands)
                    print(f"Result: {result}")
            except Exception as e:
                print(e)
