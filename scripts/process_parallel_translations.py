from datasets import load_dataset, Dataset

# Function to process unstructured data
def process_unstructured_dataset(dataset):
    organized_data = {
        "English": [],
        "Singlish": []
    }
    
    for entry in dataset['translation']:
        english_text = entry.get('en', '').strip()
        singlish_text = entry.get('sn', '').strip()
        
        if english_text and singlish_text:  # Check if both texts are not empty
            organized_data["English"].append(english_text)
            organized_data["Singlish"].append(singlish_text)

    return Dataset.from_dict(organized_data)

# Load dataset
dataset = load_dataset("Udith-Sandaruwan/english-sinhala-translated", split='train')
print(dataset)

# Process dataset
processed_dataset = process_unstructured_dataset(dataset)

# Print processed dataset
print(processed_dataset)

# Save processed dataset if needed
processed_dataset.push_to_hub("adithyasean/english-singlish-translation", private=True)