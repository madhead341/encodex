import encodex
from encodex.core import Core

class Functions:
    """Provides obfuscation and execution for Python code."""
    
    @staticmethod
    def obfuscate(code: str) -> str:
        """Obfuscates Python code using Strings encoding."""
        Core.log(f"Obfuscating Python code:\n{code}")
        encoded_code = encodex.Strings.encode(code)
        obfuscated = f'import encodex\nexec(encodex.Strings.decode(\'\'\'{encoded_code}\'\'\'))'  # Using triple single quotes
        Core.log(f"Generated obfuscated code:\n{obfuscated}")
        return obfuscated

    @staticmethod
    def save(code: str, filename: str):
        """Saves obfuscated code to a file that will run when opened."""
        Core.log(f"Saving obfuscated code to {filename}")
        obfuscated_code = Functions.obfuscate(code)
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)
        
        Core.log(f"Obfuscated code saved successfully in {filename}.")
        Core.log(f"You can now run this file to execute the obfuscated code directly.")

    @staticmethod
    def run(code: str):
        """Runs obfuscated code dynamically."""
        Core.log("Running obfuscated code...")
        obfuscated_code = Functions.obfuscate(code)
        exec(obfuscated_code)
        Core.log("Execution complete.")
