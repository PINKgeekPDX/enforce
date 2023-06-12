import os
import sys

sys.path.append('parser')

from parser.EnforceParser import EnforceParser

def preprocess_data(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    parser = EnforceParser(content)
    parsed_data = parser.parse()
    # Perform any additional cleaning and tokenization
    return parsed_data

def create_gpt_dataset(parsed_data):
    dataset = []
    for data in parsed_data:
        input_text = data['input']
        output_text = data['output']
        dataset.append({'input': input_text, 'output': output_text})
    return dataset

codebase_dir = 'rawcodebase'
parsed_data = []

for root, dirs, files in os.walk(codebase_dir):
    for file in files:
        if file.endswith('.c'):
            file_path = os.path.join(root, file)
            parsed_data.extend(preprocess_data(file_path))

gpt_dataset = create_gpt_dataset(parsed_data)