from app.commands import Command


class DivideCommand(Command):
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2
    
    def execute(self):
        if self.operand2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return self.operand1 / self.operand2
