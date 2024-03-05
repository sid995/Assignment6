class MenuCommand:
    def __init__(self, available_commands):
        self.available_commands = available_commands

    def execute(self):
        print("Available commands:")
        for command in self.available_commands:
            print(f" - {command}")
        print(" - menu")