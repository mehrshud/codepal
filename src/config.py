import logging
from typing import Dict
import os

class Config:
    """
    Configuration manager for CodePal project.

    Attributes:
        config (Dict): Dictionary containing project configuration.
    """

    def __init__(self):
        """
        Initializes the configuration manager.
        """
        self.config = {
            "debug": os.environ.get("DEBUG", False),
            "model_path": os.environ.get("MODEL_PATH", "models/model.tf"),
            "log_level": os.environ.get("LOG_LEVEL", "INFO"),
            "tf_seed": os.environ.get("TF_SEED", 42)
        }
        self.set_log_level()

    def set_log_level(self) -> None:
        """
        Sets the log level based on the configuration.
        """
        log_level = self.config["log_level"]
        logging.basicConfig(level=getattr(logging, log_level))

    def get_config(self) -> Dict:
        """
        Returns the project configuration.

        Returns:
            Dict: Dictionary containing project configuration.
        """
        return self.config

def get_config() -> Config:
    """
    Returns an instance of the configuration manager.

    Returns:
        Config: Instance of the configuration manager.
    """
    return Config()

config = get_config()
logging.info("Loaded configuration")