import io
import sys

from app.commandhandler import CommandHandler
from app.commands.menu import MenuCommand

def test_menu_command_output():
    handler = CommandHandler()
    menu_command = MenuCommand(handler.get_keys())
    handler.register_command('menu', menu_command)

    captured_output = io.StringIO()          
    sys.stdout = captured_output             
    handler.execute_command('menu')
    sys.stdout = sys.__stdout__              
    
    assert "Available commands:" in captured_output.getvalue()
