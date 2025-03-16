import string
from encodex.core import Core

class Strings:
    """Encodes and decodes strings using Base95 and bitwise manipulation, with a user-defined key (1-95)."""
    
    BASE95_CHARS = ''.join(chr(i) for i in range(32, 127))  # Printable ASCII (95 chars)
    BASE = len(BASE95_CHARS)
    key = 69  # Default key

    @staticmethod
    def set_key(new_key: int):
        """Sets the encryption key (must be between 1 and 95)."""
        if not (1 <= new_key <= 95):
            raise ValueError("Key must be between 1 and 95.")
        Strings.key = new_key
        Core.log(f"Encryption key set to {new_key}")

    @staticmethod
    def to_base95(num: int) -> str:
        """Encodes a number into Base95."""
        encoded = ""
        while num > 0:
            encoded = Strings.BASE95_CHARS[num % Strings.BASE] + encoded
            num //= Strings.BASE
        encoded = encoded.rjust(2, Strings.BASE95_CHARS[0])
        Core.log(f"Converted number {num} to Base95: {encoded}")
        return encoded

    @staticmethod
    def from_base95(encoded: str) -> int:
        """Decodes a Base95 string back to a number."""
        num = 0
        for char in encoded:
            num = num * Strings.BASE + Strings.BASE95_CHARS.index(char)
        Core.log(f"Converted Base95 {encoded} back to number: {num}")
        return num

    @classmethod
    def encode(cls, data: str) -> str:
        """Encodes a string with Base95 and bitwise manipulation using the chosen key."""
        Core.log(f"Encoding string: {data}")
        encoded_str = ""
        for char in data:
            num = ord(char)
            Core.log(f"Original ASCII ({char}): {num}")
            num = (num ^ cls.key)
            Core.log(f"After XOR with key {cls.key}: {num}")
            num = ((num << 3) | (num >> 5)) & 0xFF  # Bitwise shift
            Core.log(f"After bitwise shift: {num}")
            encoded_str += cls.to_base95(num)
        encoded_str = encoded_str[::-1]  # Reverse for obfuscation
        Core.log(f"Final encoded string: {encoded_str}")
        return encoded_str

    @classmethod
    def decode(cls, data: str) -> str:
        """Decodes a string back to its original form using the chosen key."""
        Core.log(f"Decoding string: {data}")
        data = data[::-1]  # Reverse back
        decoded_str = ""
        for i in range(0, len(data), 2):  # Process two chars at a time
            num = cls.from_base95(data[i:i+2])  # Convert Base95 back to number
            Core.log(f"Decoded Base95 segment {data[i:i+2]} to {num}")
            num = ((num >> 3) | (num << 5)) & 0xFF  # Undo bitwise shift
            Core.log(f"After reverse bitwise shift: {num}")
            num = num ^ cls.key 
            Core.log(f"After XOR with key {cls.key}: {num} ({chr(num)})")
            decoded_str += chr(num)
        Core.log(f"Final decoded string: {decoded_str}")
        return decoded_str
