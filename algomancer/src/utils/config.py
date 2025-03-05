import json
import os

# Set the environment in dev to not be in the library folder
WORKING_DIR = os.path.join(os.getcwd())
if os.getenv("ENVIRON", "prod") == "dev":
    WORKING_DIR = os.path.join(os.getcwd(), "../")
CONFIG_DIR = os.path.join(WORKING_DIR, ".algomancer_config.json")
DEFAULT_CONFIG = {
    "working_dir": WORKING_DIR,
    "solved_dir_name": os.path.join(WORKING_DIR,"solved"),
    "attempting_dir_name": os.path.join(WORKING_DIR,"attempting"),
    "data_structures_dir_name": os.path.join(WORKING_DIR,"data_structures"),
}


def load_config() -> dict:
    """Load configuration from config.json."""
    try:
        if not os.path.exists(CONFIG_DIR):
            return DEFAULT_CONFIG
        with open("config.json", "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading config: {e}")
        return {}