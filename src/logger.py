import logging
import os
from datetime import datetime

# Create the logs directory path
logs_directory = os.path.join(os.getcwd(), "logs")

# Ensure the logs directory exists
os.makedirs(logs_directory, exist_ok=True)

# Define the log file name with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the full log file path
LOG_FILE_PATH = os.path.join(logs_directory, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
