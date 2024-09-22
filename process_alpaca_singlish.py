from datasets import load_dataset, Dataset

# Function to process dataset by combining every 4 rows
def process_dataset(dataset):
    combined_data = {
        "instruction": [],
        "prompt": [],
        "response": []
    }
    
    # Iterate over the dataset in steps of 4
    for i in range(0, len(dataset), 4):
        # Make sure there are enough rows left to process
        if i + 3 < len(dataset):
            # Extract and clean up the relevant rows
            instruction = dataset[i]["text"].replace("Translated Instruction: ", "").strip()
            prompt = dataset[i + 1]["text"].replace("Translated Input: ", "").strip()
            response = dataset[i + 2]["text"].replace("Translated Output: ", "").strip()

            # Append the processed data
            combined_data["instruction"].append(instruction)
            combined_data["prompt"].append(prompt)
            combined_data["response"].append(response)

    return Dataset.from_dict(combined_data)

# Main script
dataset = load_dataset("adithyasean/alpaca-singlish", split='train')

# Process the dataset
processed_dataset = process_dataset(dataset)

# Save processed dataset if needed
processed_dataset.push_to_hub("adithyasean/alpaca-singlish", private=True)