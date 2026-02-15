import logging
import os
from typing import Dict

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("codepal.log"), logging.StreamHandler()]
)

# Load configuration from environment variables
class Config:
    def __init__(self):
        self.api_key: str = os.environ.get("CODEPAL_API_KEY")
        self.tf_model_path: str = os.environ.get("CODEPAL_TF_MODEL_PATH")
        self.react_app_url: str = os.environ.get("CODEPAL_REACT_APP_URL")

        if not self.api_key:
            raise ValueError("CODEPAL_API_KEY environment variable is not set")
        if not self.tf_model_path:
            raise ValueError("CODEPAL_TF_MODEL_PATH environment variable is not set")
        if not self.react_app_url:
            raise ValueError("CODEPAL_REACT_APP_URL environment variable is not set")

    def get_config(self) -> Dict[str, str]:
        return {
            "api_key": self.api_key,
            "tf_model_path": self.tf_model_path,
            "react_app_url": self.react_app_url,
        }

# Initialize configuration
config: Config = Config()

# Set up logging for configuration load
logging.info("Loaded configuration successfuly")
logging.info(config.get_config())