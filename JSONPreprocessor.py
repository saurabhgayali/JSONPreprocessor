import json

class JSONPreprocessor:
    def __init__(self, json_data, arguments):
        self.json_data = json_data
        self.arguments = arguments

    def extract_fields(self, data, fields):
        parsed_data = {}

        for field in fields:
            if field in data:
                parsed_data[field] = data[field]

        return parsed_data

    def preprocess_json(self):
        data = json.loads(self.json_data)
        parsed_data = {}

        parsed_data.update(self.extract_fields(data, self.arguments))

        for key, value in data.items():
            if isinstance(value, dict):
                parsed_value = self.extract_fields(value, self.arguments)
                if parsed_value:
                    parsed_data[key] = parsed_value

            if isinstance(value, list):
                parsed_data[key] = []
                for item in value:
                    if isinstance(item, dict):
                        parsed_item = self.extract_fields(item, self.arguments)
                        if parsed_item:
                            parsed_data[key].append(parsed_item)

                    if isinstance(item, list):
                        parsed_data[key].extend(self.preprocess_nested_list(item, self.arguments))

        final_json = json.dumps(parsed_data)

        return final_json

    def preprocess_nested_list(self, nested_list, arguments):
        parsed_list = []
        for item in nested_list:
            if isinstance(item, dict):
                parsed_item = self.extract_fields(item, arguments)
                if parsed_item:
                    parsed_list.append(parsed_item)

            if isinstance(item, list):
                parsed_list.extend(self.preprocess_nested_list(item, arguments))
        return parsed_list


if __name__ == "__main__":
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

    # Print the final preprocessed JSON
    print(preprocessed_json)
