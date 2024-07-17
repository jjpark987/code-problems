import re
import json

def parse_py_file(file_path):
    try:
        # Open file as 'read'
        with open(file_path, 'r') as file:
            content = file.read()

        # Extract the comment block
        comment_block = re.search(r'("""[\s\S]*?""")', content)

        if not comment_block:
            raise ValueError("No comment block found")

        comment = comment_block.group().strip('"""').strip()

        # Define patterns for each field
        patterns = {
            'category': r'category:\s*(.*)',
            'subcategory': r'subcategory:\s*(.*)',
            'difficulty': r'difficulty:\s*(.*)',
            'image_url_e1': r'image_url_e1:\s*(.*)',
            'image_url_e2': r'image_url_e2:\s*(.*)',
            'image_url_e3': r'image_url_e3:\s*(.*)',
            'title': r'title:\s*(.*)',
            'description': r'description:\s*((.|\n)+?)\n\nExample',
            'example1': r'Example 1:\s*((.|\n)+?)(Example 2:|$)',
            'example2': r'Example 2:\s*((.|\n)+?)(Example 3:|Constraints:|$)',
            'example3': r'Example 3:\s*((.|\n)+?)(Constraints:|$)',
            'constraints': r'Constraints:\s*((.|\n)+?)$'
        }

        # Extract information using regex patterns
        parsed_data = {}

        for field, pattern in patterns.items():
            match = re.search(pattern, comment)
            if match:
                if field.startswith('image_url'):
                    image_url = match.group(1)
                    if image_url.lower() == 'none':
                        parsed_data[field] = None
                    else:
                        parsed_data[field] = image_url
                elif field.startswith('example'):
                    example_content = match.group(1)
                    example_content = re.sub(r'^\s*/python/images/.+\n\n', '', example_content)
                    parsed_data[field] = example_content.strip()
                else:
                    parsed_data[field] = match.group(1)
            else:
                parsed_data[field] = None

        # Convert to JSON
        json_data = json.dumps(parsed_data, indent=4)
        
        return json_data

    except Exception as e:
        print(f"Error occurred: {e}")

# Test parse.py on main.py
if __name__ == '__main__':
    file_path = '../main.py'
    data = parse_py_file(file_path)
    if data:
        print(data)
