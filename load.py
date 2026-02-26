import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(data, file_name):
    """Saves the DataFrame to a CSV file."""
    logging.info(f'Loading data into file: {file_name}')
    data.to_csv(file_name, index=False)
    return data