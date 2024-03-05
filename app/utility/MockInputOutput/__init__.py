from unittest.mock import patch
from io import StringIO

class MockInputOutput:
    def __init__(self, inputs):
        self.inputs = inputs
        self.output = StringIO()

    def __enter__(self):
        self.input_patch = patch('builtins.input', side_effect=self.inputs)
        self.input_mock = self.input_patch.start()

        self.output_patch = patch('sys.stdout', new=self.output)
        self.output_patch.start()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.input_patch.stop()
        self.output_patch.stop()

    def get_output(self):
        return self.output.getvalue()