# JSON Preprocessor

The JSON Preprocessor is a Python script that allows you to extract specific data fields from a JSON document, including both common data and nested data.

## Usage

1. Clone the repository:

  ```git clone <repository_url>```

2. Install the required dependencies (assuming you have Python and pip installed):

```pip install -r requirements.txt```

3. Run the script:
```python json_preprocessor.py```
5. Modify the json_data variable in json_preprocessor.py to provide your own JSON data.

6. Specify the arguments to extract from the JSON data by modifying the arguments list in json_preprocessor.py.

7. Execute the script to preprocess the JSON data and obtain the desired output.

## Examples
### Example JSON Data
```
{
    "id": 1,
    "name": "John Doe",
    "age": 30,
    "nested_data": [
        {
            "city": "New York",
            "occupation": "Engineer",
            "hobby": "Photography",
            "contacts": [
                {
                    "type": "email",
                    "value": "john@example.com"
                },
                {
                    "type": "phone",
                    "value": "123-456-7890"
                }
            ]
        },
        {
            "city": "Los Angeles",
            "occupation": "Designer",
            "hobby": "Painting",
            "contacts": [
                {
                    "type": "email",
                    "value": "jane@example.com"
                },
                {
                    "type": "phone",
                    "value": "987-654-3210"
                }
            ]
        }
    ],
    "email": "john@example.com"
}
```
### Specify Arguments
To extract specific fields, modify the arguments list in json_preprocessor.py:

```arguments = ["id", "name", "nested_data", "city", "occupation", "contacts", "type", "value"]```

In this example, the script will extract the following fields:

Common data: id, name
* Nested data: nested_data, city, occupation, contacts, type, value
* The resulting preprocessed JSON will include the extracted fields.

## Importing as Library
Here's an example of how to use the JSON Preprocessor as a library:

```
from json_preprocessor import JSONPreprocessor

# Example JSON data with nested occurrences and main-level data
json_data = '''
{
    "id": 1,
    "name": "John Doe",
    "age": 30,
    "nested_data": [
        {
            "city": "New York",
            "occupation": "Engineer",
            "hobby": "Photography",
            "contacts": [
                {
                    "type": "email",
                    "value": "john@example.com"
                },
                {
                    "type": "phone",
                    "value": "123-456-7890"
                }
            ]
        },
        {
            "city": "Los Angeles",
            "occupation": "Designer",
            "hobby": "Painting",
            "contacts": [
                {
                    "type": "email",
                    "value": "jane@example.com"
                },
                {
                    "type": "phone",
                    "value": "987-654-3210"
                }
            ]
        }
    ],
    "email": "john@example.com"
}
'''

# Specify the arguments to extract from the JSON data
arguments = ["id", "name", "nested_data", "city", "occupation", "contacts", "type", "value"]

# Create an instance of JSONPreprocessor
preprocessor = JSONPreprocessor(json_data, arguments)

# Preprocess the JSON data
preprocessed_json = preprocessor.preprocess_json()

# Use the preprocessed JSON as needed
print(preprocessed_json)

```

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
