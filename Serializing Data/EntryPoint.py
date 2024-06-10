from generate_key import generate_key
from deserialize import deserialize 
from serialize import serialize

def safe_deserialize(key, serialized_data):  
    new_key = generate_key(serialized_data) 
  
    print(f"key = {key}")
  
    try:
        if key == new_key:
            return deserialize(serialized_data)
        else:
            raise Exception('New key does not match old key') 
    except Exception as error:
        print('Error:', error)
        
    return False

# Example usage
grades = {'Alice': 89, 'Bob': 72, 'Charles': 87}
serialized_data = serialize(grades)
deserialized_data = safe_deserialize(generate_key(serialized_data), serialized_data)

