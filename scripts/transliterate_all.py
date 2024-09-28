from sinhala_to_singlish import sinhala_to_singlish
from huggingface_hub import login
login()
from datasets import load_dataset, DatasetDict

input_dataset_repository = input("Enter the Hugging Face dataset repository name: ")
output_dataset_repository = input("Enter the Hugging Face dataset repository name to push the transliterated dataset: ")

dataset = load_dataset(input_dataset_repository)

def transliterate_example(example):
    return {key: sinhala_to_singlish(value) if isinstance(value, str) else value for key, value in example.items()}

transliterated_splits = {}
for split in dataset.keys():
    transliterated_splits[split] = dataset[split].map(transliterate_example)

transliterated_dataset = DatasetDict(transliterated_splits)
transliterated_dataset.push_to_hub(output_dataset_repository, private=True)