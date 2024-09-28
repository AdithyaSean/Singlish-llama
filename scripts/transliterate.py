from sinhala_to_singlish import sinhala_to_singlish
from datasets import load_dataset, DatasetDict

input_dataset_repository = input("Enter the Hugging Face dataset repository name: ")

dataset = load_dataset(input_dataset_repository)
print(dataset)
print(dataset["train"][0])
field_to_transliterate = input("Enter the field to transliterate: ")
new_field_name = input("Enter the new field name: ")

transliterated_splits = {}
for split in dataset.keys():
    transliterated_splits[split] = dataset[split].map(lambda example: {
        new_field_name: sinhala_to_singlish(example[field_to_transliterate])
    })

transliterated_dataset = DatasetDict(transliterated_splits)
print(transliterated_dataset)
print(transliterated_dataset["train"][0])

output_dataset_repository = input("Enter the Hugging Face dataset repository name to push the transliterated dataset: ")
if output_dataset_repository:
    transliterated_dataset.push_to_hub(output_dataset_repository, private=True)
    print("Transliterated dataset pushed to the Hugging Face Hub.")
else:
    print("Transliterated dataset not pushed to the Hugging Face Hub.")