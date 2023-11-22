import json

def extract_strings(json_data):
    extracted_strings = []
    strings_dict = json_data.get("strings", {})

    for key, value in strings_dict.items():
        extracted_strings.append(key)

    return extracted_strings

# Get the JSON data from the file
json_data = open("data.json").read()

# Parse the JSON data
parsed_json = json.loads(json_data)

# Extract strings
result = extract_strings(parsed_json)

# Print the extracted strings
for string in result:
    print(string)
