import logging
from typing import Dict
import os

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

def load_config() -> Dict:
    """
    Load configuration from environment variables.
    
    Returns:
        Dict: Configuration dictionary
    """
    try:
        config = {
            "TF_MODEL_PATH": os.environ["TF_MODEL_PATH"],
            "REACT_APP_URL": os.environ["REACT_APP_URL"]
        }
        return config
    except KeyError as e:
        logging.error(f"Error loading configuration: {e}")
        raise

def validate_config(config: Dict) -> None:
    """
    Validate configuration dictionary.
    
    Args:
        config (Dict): Configuration dictionary
    
    Raises:
        ValueError: If configuration is invalid
    """
    if not config:
        raise ValueError("Configuration cannot be empty")
    required_keys = ["TF_MODEL_PATH", "REACT_APP_URL"]
    if not all(key in config for key in required_keys):
        raise ValueError("Missing required configuration keys")

def get_config() -> Dict:
    """
    Get validated configuration dictionary.
    
    Returns:
        Dict: Validated configuration dictionary
    """
    config = load_config()
    validate_config(config)
    return config

config = get_config()