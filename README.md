# Encodex

Encodex is a Python package for string encoding/encryption. It provides a custom **Base95** encoding method, designed to help with basic obfuscation or encryption tasks.

## Features:
- **Base95 encoding** for string obfuscation.
- **Python code obfuscation**: Encode Python code to make it less readable.
- **Cross-platform**: Works on both Windows and macOS.
- **Detailed error logging**: Logs errors for debugging and troubleshooting.

## Installation

To install **Encodex**, run the following command:

```bash
pip install encodex
```

## Initializing
For debugging, use Core.set_debug
```py
Core.set_debug(state=True, log_to_file=True)
```

For setting the EncodeX decryption key, use encodex.Strings.set_key
```py
encodex.Strings.set_key(key) # key is 1-95 (default key is 69)
```

## Usage
For encoding and decoding strings, use
```py
# Encode a string
import encodex
from encodex import Strings

# Encode a string
encoded = encodex.Strings.encode("Hello World")

# Decode the encoded string
decoded = encodex.Strings.decode(encoded)

print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")
```
