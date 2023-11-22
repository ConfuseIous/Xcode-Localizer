import json

# Your string of sentences separated by newlines
# NOTE: The first line should be on the same as the declaration of the variable, otherwise the first sentence will be empty.
sentence_str = """Cancelar
Conexión
Error
Eventos
"""

sentences = sentence_str.split("\n")

should_trim = True # Set to True if you want to remove all leading and trailing spaces from the sentences
file_name = "data.json"
language_key = "es"

with open(file_name, "r", encoding="utf-8") as input_file:
    json_data = json.load(input_file)
    
    original_sentences = json_data["strings"].keys()

    # For each original_sentence, add the correspoding sentence, in a new subkey called "de" under localizations under the original_sentence
    # Add in this format: 
    #    "de": {
    #    "stringUnit": {
    #        "state": "translated",
    #        "value": sentence
    #    }
    #}
    for original_sentence, sentence in zip(original_sentences, sentences):
        if should_trim:
            sentence = sentence.strip()
        json_data["strings"][original_sentence]["localizations"][language_key] = {
            "stringUnit": {
                "state": "translated",
                "value": sentence
            }
        }

with open(file_name, "w", encoding="utf-8") as output_file:
    json.dump(json_data, output_file, ensure_ascii=False, indent=4)
