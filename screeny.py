import pyautogui
import time
import threading
import tkinter as tk

# Define the screenshot function
def take_screenshots():
    x = 0
    y = 0
    width = 1920
    height = 1080
    i = 0

    while not stop_screenshot.is_set():  # Loop until stopped
        time.sleep(5)
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        screenshot.save(f'screenshot_{i}.png')
        i += 1

# Function to stop the screenshots
def stop():
    stop_screenshot.set()

# Create a flag to signal when to stop
stop_screenshot = threading.Event()

# Start the screenshot function in a separate thread
screenshot_thread = threading.Thread(target=take_screenshots)
screenshot_thread.start()

# Create a GUI window
root = tk.Tk()
root.title("Screenshot Controller")

# Add a Stop button
stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack()

# Start the GUI event loop
root.mainloop()
