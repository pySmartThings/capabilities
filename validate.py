import json

def validate_no_duplicates(file_path):
    with open(file_path, 'r') as f:
        capabilities = json.load(f)

    duplicates = set([capability for capability in capabilities if capabilities.count(capability) > 1])

    if duplicates:
        print(f"Duplicate capabilities found: {duplicates}")
    else:
        print("No duplicates found.")

if __name__ == '__main__':
    validate_no_duplicates('capabilities.json')