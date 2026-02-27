import sys
from extract import extract_data
from transform import add_missing_columns, sort_data, generate_statistics
from load import load_data
from config import INPUT_CSV, OUTPUT_EXTENDED_CSV, OUTPUT_STATS_CSV

def check_empty(df):
    """Checks if DataFrame is empty and exits pipeline if true."""
    if df.empty:
        print("Input CSV is empty! Exiting pipeline.")
        sys.exit(1)
    return df

df = (extract_data(INPUT_CSV)
      .pipe(check_empty)
      .pipe(add_missing_columns)
      .pipe(sort_data))

stats_df = generate_statistics(df)

df = load_data(df, OUTPUT_EXTENDED_CSV)
stats_df = load_data(stats_df, OUTPUT_STATS_CSV)

