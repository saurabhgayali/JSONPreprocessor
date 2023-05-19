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
