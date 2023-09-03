import tkinter as tk
from tkinter import messagebox  
import time
import winsound

def ring_alarm():
    label.config(text="Alarm Rang!")  # Display a message when the alarm rings
    messagebox.showinfo("Alarm", "Time To Wake Up!\nAlarm rang!", icon='info', parent=root)  # Display the message box

def set_alarm():
    alarm_time = entry.get()
    try:
        time.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please use HH:MM:SS.")
        return

    set_button.config(state=tk.DISABLED)  # Disable the button after setting the alarm

    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            winsound.Beep(2000, 3000)  # Beep for 3 seconds at 1000 Hz
            ring_alarm()
            break
        root.update()  # Update the GUI to show the current time
        time.sleep(1)  # Wait for 1 second

root = tk.Tk()
root.title("Simple Alarm Clock")

label = tk.Label(root, text="Enter the time in 24-hour format (HH:MM:SS):")
label.pack()

entry = tk.Entry(root)
entry.pack()

set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack(pady=10)

root.mainloop()
