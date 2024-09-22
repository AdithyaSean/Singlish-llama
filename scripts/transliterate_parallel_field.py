from scripts.sinhala_to_singlish import sinhala_to_singlish
from datasets import load_dataset, DatasetDict
import re

# Function to remove specified prefixes from text
def remove_prefixes(text):
    prefixes = ["Translated Instruction: ", "Translated Input", "Translated Output"]
    for prefix in prefixes:
        if text.startswith(prefix):
            text = text[len(prefix):]
    return text

# Function to clean and transliterate text
def clean_and_transliterate(text):
    text = remove_prefixes(text)
    text = sinhala_to_singlish(text)
    return text

def push_to_huggingface():
    input_dataset_repository = input("Enter the Hugging Face dataset repository name: ")
    output_dataset_repository = input("Enter the Hugging Face dataset repository name to push the transliterated dataset: ")

    dataset = load_dataset(input_dataset_repository)

    transliterated_splits = {}
    for split in dataset.keys():
        transliterated_splits[split] = dataset[split].map(lambda example: {
            "instruction": clean_and_transliterate(example["instruction"]),
            "prompt": clean_and_transliterate(example["prompt"]),
            "response": clean_and_transliterate(example["response"])
        })

    transliterated_dataset = DatasetDict(transliterated_splits)
    transliterated_dataset.push_to_hub(output_dataset_repository, private=True)

push_to_huggingface()