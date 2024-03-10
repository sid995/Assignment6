# test_app.py (continued)
from app import App

def test_load_environment_variables(monkeypatch):
    # Setup: Define a mock environment variable
    monkeypatch.setenv('TEST_VARIABLE', '12345')

    # Action: Initialize the app and load environment variables
    app = App()
    settings = app.load_environment_variables()

    # Assert: Check if the environment variable is loaded correctly
    assert 'TEST_VARIABLE' in settings
    assert settings['TEST_VARIABLE'] == '12345'
