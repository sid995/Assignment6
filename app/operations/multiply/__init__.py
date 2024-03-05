from app.commands import Command


class MultiplyCommand(Command):
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2
    
    def execute(self):
        return self.operand1 * self.operand2