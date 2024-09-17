import pandas as pd

def convert_parquet_to_jsonl(parquet_file, jsonl_file):
    # Read the Parquet file into a DataFrame
    df = pd.read_parquet(parquet_file)
    
    # Write the DataFrame to a JSON Lines file
    df.to_json(jsonl_file, orient='records', lines=True, force_ascii=False)

# Example usage
parquet_file = input("input file: ")
jsonl_file = input("output file: ")
convert_parquet_to_jsonl(parquet_file, jsonl_file)