# Ethical Keylogger (Educational Only)

**DISCLAIMER**  
This project is strictly for **educational and ethical purposes only**.  
Using keyloggers on systems or individuals without proper authorisation is **illegal** and may result in serious legal consequences.  
Use responsibly and only in environments where you have **explicit consent** (e.g. cybersecurity labs, personal testing, or portfolio demonstrations like this).  

---

## Overview  
This is a simple ethical keylogger written in Python.  
It captures keystrokes and:  
- writes them to a log file (`keylog.txt`) at regular intervals  
- displays them live inside a **Tkinter GUI window**  

The project was built as a way to practise event handling, file writing, threading, and creating a basic graphical interface. It demonstrates how keylogging works in a **controlled and authorised environment**.  

---

## Features  
- Logs all keystrokes with timestamps  
- Handles special keys (Enter, Space, etc.)  
- Automatically writes logs to `keylog.txt` at set intervals  
- User consent check before starting  
- **Graphical User Interface (GUI):**  
  - Start and Stop buttons for easy control  
  - Pop-up consent reminder  
  - Live keystroke viewer inside the application window  

---

## Requirements  
- Python 3.7+  
- The following Python libraries:  
  - [`keyboard`](https://pypi.org/project/keyboard/) (for capturing keystrokes)  
  - [`tkinter`](https://docs.python.org/3/library/tkinter.html) (comes with Python, used for the GUI)  

Install dependencies with:  
```bash
pip install keyboard

Future Improvements

Add a server viewer to monitor logs remotely (with proper security).

Create a web-based GUI viewer for integration into a personal website.