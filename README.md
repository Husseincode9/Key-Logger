# Ethical Keylogger (Educational Only)

**DISCLAIMER**  
This project is strictly for **educational and ethical purposes only**.  
Using keyloggers on systems or individuals without proper authorization is **illegal** and may result in severe legal consequences.  
Use responsibly and only in environments where you have **explicit consent** (e.g., cybersecurity labs, personal testing, or portfolio demonstrations).

---

##Overview
This is a simple ethical keylogger written in Python.  
It captures keystrokes and writes them to a log file (`keylog.txt`) at regular intervals.  
The script is designed to demonstrate how keylogging works in a **controlled and authorized environment**.

---

## Features
- Logs all keystrokes with timestamps.
- Handles special keys (Enter, Space, etc.).
- Automatically writes logs to `keylog.txt` at set intervals.
- User consent check before starting.

---

## Requirements
- Python 3.7+
- The following Python libraries:
  - [`keyboard`](https://pypi.org/project/keyboard/)

Install dependencies with:
```bash
pip install keyboard
