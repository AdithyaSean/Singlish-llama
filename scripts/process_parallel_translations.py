from datasets import load_dataset, Dataset

# Function to process unstructured data
def process_unstructured_dataset(dataset):
    organized_data = {
        "English": [],
        "Sinhala": []
    }
    
    for entry in dataset['translation']:
        english_text = entry.get('en', '').strip()
        singlish_text = entry.get('sn', '').strip()
        
        if english_text and singlish_text:  # Check if both texts are not empty
            organized_data["English"].append(english_text)
            organized_data["Sinhala"].append(singlish_text)

    return Dataset.from_dict(organized_data)

# Load dataset
dataset_name = input("Enter the Hugging Face dataset repository name: ")
save_dataset_to = input("Enter the Hugging Face dataset repository name to push the processed dataset: ")
dataset = load_dataset(dataset_name, split='train')
print(dataset)

# Process dataset
processed_dataset = process_unstructured_dataset(dataset)

# Print processed dataset
print(processed_dataset)

# Save processed dataset if needed
processed_dataset.push_to_hub(save_dataset_to, private=True)