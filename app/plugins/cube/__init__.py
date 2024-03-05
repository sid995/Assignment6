from app.commands import Command

class CubeCommand(Command):
    def __init__(self, operand):
        self.operand = operand

    def execute(self):
        return self.operand * self.operand * self.operand