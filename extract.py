import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_data(file_name):
    """Loads a CSV file with city coordinates and returns a Pandas DataFrame."""
    try:
        logging.info(f"Loading CSV file: {file_name}")
        data = pd.read_csv(file_name)
        logging.info(f"Loaded {len(data)} rows from {file_name}")
        return data
    
    except FileNotFoundError:
        logging.error(f"File {file_name} not found!")
        return pd.DataFrame()
    except pd.errors.ParserError:
        logging.error(f"File {file_name} could not be parsed!")
        return pd.DataFrame()
    except Exception as e:
        logging.error(f"Unexpected error while reading {file_name}: {e}")
        return pd.DataFrame()