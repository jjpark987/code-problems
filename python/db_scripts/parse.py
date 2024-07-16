import re
import json

def parse_file(file_path):
    # Step 1: Open the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Step 2: Define patterns for each field
    patterns = {
        'category': r'category:\s*(.+)',
        'subcategory': r'subcategory:\s*(.+)',
        'difficulty': r'difficulty:\s*(.+)',
        'image_url_e1': r'image_url_e1:\s*(.+)',
        'image_url_e2': r'image_url_e2:\s*(.+)',
        'title': r'title:\s*(.+)',
        'description': r'description:\s*((.|\n)+?)\n\nExample',
        'example1': r'Example 1:\s*((.|\n)+?)Example 2:',
        'example2': r'Example 2:\s*((.|\n)+?)(Example 3:|Constraints:|$)',
        'example3': r'Example 3:\s*((.|\n)+?)(Constraints:|$)',
        'constraints': r'Constraints:\s*((.|\n)+?)\n*\"\"\"'
    }

    # Step 3: Extracted data dictionary to store parsed information
    extracted_data = {}

    # Step 4: Extract information using regex patterns
    for field, pattern in patterns.items():
        match = re.search(pattern, content)
        if match:
            extracted_data[field] = match.group(1).strip()
        else:
            extracted_data[field] = None

    # Step 5: Convert extracted_data to JSON format
    json_data = json.dumps(extracted_data, indent=4)
    print(json_data)  # Optionally print JSON data

    return extracted_data

# Example usage:
if __name__ == '__main__':
    file_path = 'main.py'  # Replace with your file path
    data = parse_file(file_path)