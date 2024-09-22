from transliterate import sinhala_to_singlish
from datasets import load_dataset, DatasetDict

def push_to_huggingface():
    input_dataset_repository = input("Enter the Hugging Face dataset repository name: ")
    output_dataset_repository = input("Enter the Hugging Face dataset repository name to push the transliterated dataset: ")
    api_token = input("Enter your Hugging Face API token: ")

    dataset = load_dataset(input_dataset_repository)

    transliterated_splits = {}
    for split in dataset.keys():
        transliterated_splits[split] = dataset[split].map(lambda example: {"text": sinhala_to_singlish(example["text"])})

    transliterated_dataset = DatasetDict(transliterated_splits)
    transliterated_dataset.push_to_hub(output_dataset_repository, token=api_token, private=True)

push_to_huggingface()