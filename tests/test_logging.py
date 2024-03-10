# test_app.py
from unittest.mock import patch
from app import App

def test_configure_logging_with_file(mocker, tmp_path):
    # Setup: Create a dummy logging config file
    config_file = tmp_path / "logging.conf"
    config_file.write_text("[loggers]\nkeys=root\n")

    # Use mocker to patch os.path.exists and logging.config.fileConfig
    mocker.patch('os.makedirs')
    mocker.patch('os.path.exists', return_value=True)

    # Initialize App and call configure_logging
    with patch('logging.config.fileConfig') as mock_fileConfig:
        app = App()
        app.configure_logging()

        # Assert that fileConfig was called with the expected file path
        mock_fileConfig.assert_called_with(str(config_file))



def test_configure_logging_without_file(caplog):
    # Setup: Ensure the logging configuration file does not exist
    with patch('os.makedirs'), patch('os.path.exists', return_value=False):
        app = App()
        app.configure_logging()

    # Assert: Verify that fallback logging is used and checks the log level
    assert "Fallback logging configured" in caplog.text
    assert any(record.levelname == 'INFO' for record in caplog.records)
