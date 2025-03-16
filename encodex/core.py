import logging
import os
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

class Core:
    """Handles core settings and utilities for Encodex."""
    
    debug = True  # Debug (Default = True)
    
    user_home = os.path.expanduser("~")
    log_file = os.path.join(user_home, "encodex.log")  # Log file

    @staticmethod
    def set_debug(state: bool, log_to_file: bool = False):
        """Enables or disables debug mode and controls logging output."""
        Core.debug = state
        
        log_format = "[Encodex DEBUG] %(message)s"
        
        if log_to_file:
            logging.basicConfig(level=logging.DEBUG, format=log_format, filename=Core.log_file, filemode="a")
            logging.debug("Debug mode enabled, logging to encodex.log.")
        else:
            logging.basicConfig(level=logging.DEBUG, format=log_format)
            logging.debug("Debug mode enabled, logging to console.")
        
    @staticmethod
    def log(message: str):
        """Logs a debug message if debug mode is enabled."""
        if Core.debug:
            logging.debug(message)

    @staticmethod
    def handle_error(e: Exception):
        """Handles errors by printing them in red and logging them to a file."""
        error_message = f"Error: {str(e)}"
        print(Fore.RED + f"Error occurred: {type(e).__name__} - {e}")
        print(Fore.RED + f"Error log saved at: {Core.log_file}")
        
        logging.error(f"Error occurred: {type(e).__name__} - {e}")
