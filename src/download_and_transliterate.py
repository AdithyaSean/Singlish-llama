import json
import re
from datasets import load_dataset, DatasetDict
from huggingface_hub import HfApi, HfFolder

def sinhala_to_singlish(sinhala_text):
    vowels = {'අ': 'a', 'ආ': 'aa', 'ඇ': 'a', 'ඈ': 'aa', 'ඉ': 'i', 'ඊ': 'ee', 'උ': 'u', 'ඌ': 'uu','ඍ': 'ru', 'ඎ': 'ruu', 'ඏ': 'lu', 'ඐ': 'luu', 'එ': 'e', 'ඒ': 'ee', 'ඓ': 'ai', 'ඔ': 'o','ඕ': 'oo', 'ඖ': 'au', 'ං': 'n', 'ඃ': 'h'}
    consonants = {'ක': 'k', 'ඛ': 'kh', 'ග': 'g', 'ඟ': 'ng', 'ඝ': 'gh', 'ඞ': 'ng', 'ච': 'ch', 'ඡ': 'ch', 'ජ': 'j', 'ඣ': 'jh', 'ඤ': 'ny', 'ඥ': 'gny', 'ට': 't', 'ඨ': 't', 'ඩ': 'd', 'ඬ': 'nd', 'ඪ': 'd', 'ණ': 'n', 'ත': 'th', 'ථ': 'th', 'ද': 'd', 'ඳ': 'nd', 'ධ': 'dh', 'න': 'n', 'ප': 'p', 'ඵ': 'p', 'බ': 'b', 'භ': 'bh', 'ඹ': 'mba', 'ම': 'm', 'ය': 'y', 'ර': 'r', 'ල': 'l', 'ව': 'w', 'ශ': 'sh', 'ෂ': 'sh', 'ස': 's','හ': 'h', 'ළ': 'l', 'ෆ': 'f'}
    vowel_modifiers = {'්': '', 'ා': 'a', 'ැ': 'a', 'ෑ': 'a', 'ි': 'i', 'ී': 'i', 'ු': 'u', 'ූ': 'u','ෙ': 'e', 'ේ': 'e', 'ෛ': 'ai', 'ො': 'o', 'ෝ': 'o', 'ෞ': 'au','ෟ': 'ru', 'ෳ': 'ruu', '්‍ය': 'ya', 'ෘ': 'ru'}
    characters_to_remove = r'[\u200B-\u200F\u202A-\u202E\u2060-\u2064\u2065-\u2069\u206A-\u206F\uFEFF\uFFF9-\uFFFD]'
    singlish_text = ""
    i = 0

    while i < len(sinhala_text):
        if sinhala_text[i] in vowels:
            singlish_text += vowels.get(sinhala_text[i])
            i += 1

        elif sinhala_text[i] in consonants:
            singlish_text += consonants.get(sinhala_text[i])
            i += 1

            if i < len(sinhala_text) and sinhala_text[i] in vowel_modifiers:
                singlish_text += vowel_modifiers.get(sinhala_text[i])
                i += 1

                if i < len(sinhala_text) and sinhala_text[i] in vowel_modifiers:
                    singlish_text += vowel_modifiers.get(sinhala_text[i])
                    i += 1

            else:
                singlish_text += 'a'

        else:
            singlish_text += sinhala_text[i]
            i += 1

    singlish_text = re.sub(characters_to_remove, '', singlish_text)
    return singlish_text

def transliterate_value(value):
    if isinstance(value, str):
        return sinhala_to_singlish(value)
    elif isinstance(value, dict):
        return {k: transliterate_value(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [transliterate_value(item) for item in value]
    else:
        return value

def transliterate_dataset(dataset, text_column):
    def transliterate_example(example):
        example[text_column] = transliterate_value(example[text_column])
        return example

    return dataset.map(transliterate_example)

# Load dataset from Hugging Face
dataset_name = "9wimu9/sinhala_dataset_59m"
dataset = load_dataset(dataset_name)

# Specify the column containing the Sinhala text
text_column = input("Enter the name of the column containing Sinhala text: ")

# Process each split in the dataset
transliterated_dataset = DatasetDict()
for split in dataset.keys():
    transliterated_dataset[split] = transliterate_dataset(dataset[split], text_column)

# Save the transliterated dataset back to Hugging Face
output_dataset_name = "adithyasean/singlish"

# Authenticate using the API token
api = HfApi()
api_token = "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"
HfFolder.save_token(api_token)

# Push the dataset to the hub
transliterated_dataset.push_to_hub(output_dataset_name, token=api_token)