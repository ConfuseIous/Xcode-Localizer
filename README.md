# iOS - Localiser

## A simple script to localize your Localizable.xcstrings file with ChatGPT

## Usage
1. Open your Localizable.xcstrings file with a text editor and copy it into data.json.
2. The ChatGPT API costs money and isn't really necessary here, so instead, use extract.py to extract all strings from your project and translate them with ChatGPT.
Example prompt:
```
"Please help me translate all these sentences into german:"
```
3. Copy the output into the sentence_str variable in merge.py
4. Specify your language_key in merge.py
5. Run merge.py. This will update your data.json file.
6. Open your Localizable.xcstrings file with a text editor and replace its contents with the output of merge.py (which you will find in data.json)

To add more languages, repeat steps 2-5, and then finish off with 6.

## Contributing
Pull requests are welcome. I did all this in like 30min so there are almost certainly edge cases I haven't thought of.

## License
[MIT](https://choosealicense.com/licenses/mit/)
