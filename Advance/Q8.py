import re

def parse_encoded_string(encoded_str):
    pattern = r"([^0]+)0+([^0]+)0+([^0]+)"
    match = re.match(pattern, encoded_str)

    if match:
        first_name, last_name, id_value = match.groups()
        result = {
            "first_name": first_name.strip(),
            "last_name": last_name.strip(),
            "id": id_value.strip()
        }
        return result
    else:
        return None

# Example usage:
encoded_str = "Robert000Smith000123"
parsed_data = parse_encoded_string(encoded_str)
print(parsed_data)
