import sinhala_to_singlish
from datasets import load_dataset, DatasetDict

input_dataset_repository = input("Enter the Hugging Face dataset repository name: ")
output_dataset_repository = input("Enter the Hugging Face dataset repository name to push the transliterated dataset: ")

dataset = load_dataset(input_dataset_repository)

transliterated_splits = {}
for split in dataset.keys():
    transliterated_splits[split] = dataset[split].map(lambda example: {"text": sinhala_to_singlish(example["text"])})

transliterated_dataset = DatasetDict(transliterated_splits)
transliterated_dataset.push_to_hub(output_dataset_repository, private=True)