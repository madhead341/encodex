import encodex
from encodex.strings import Strings

encoded_string = input("Enter the string you want to decode: ")

key = input("Enter the decoding key (1-95): ") 

# Ensure key is a valid int between 1 and 95
while not (key.isdigit() and 1 <= int(key) <= 95):
    print("Invalid key. Please enter a number between 1 and 95.")
    key = input("Enter the decoding key (1-95): ")

# Set the decoding key
Strings.set_key(int(key))

# Decode
decoded_string = Strings.decode(encoded_string)
print(f"Decoded string: {decoded_string}")
