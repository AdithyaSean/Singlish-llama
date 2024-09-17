import os
import json

def combine_jsonl_files(input_folder, output_file):
    combined_data = []

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.jsonl'):
            file_path = os.path.join(input_folder, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    json_obj = json.loads(line)
                    combined_data.append(json_obj)

    # Write combined data to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for json_obj in combined_data:
            outfile.write(json.dumps(json_obj) + '\n')

# Example usage
input_folder = input("input folder path: ")
output_file = input("output file path: ")
combine_jsonl_files(input_folder, output_file)