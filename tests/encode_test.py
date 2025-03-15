import encodex
from encodex.strings import Strings

input_string = input("Enter the string you want to encode: ")

# Ask for the key, default to 69
key = input("Enter the encoding key (1-95): ")

# Ensure key is a valid integer between 1 and 95
while not (key.isdigit() and 1 <= int(key) <= 95):
    print("Invalid key. Please enter a number between 1 and 95.")
    key = input("Enter the encoding key (1-95): ")

# Set the encoding key
Strings.set_key(int(key))

# Encode
encoded_string = Strings.encode(input_string)
print(f"Encoded string: {encoded_string}")
