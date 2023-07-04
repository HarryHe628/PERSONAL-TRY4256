import time
from tkinter import messagebox

def start_focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        time_remaining = f"Time remaining: {seconds // 60} minutes {seconds % 60} seconds"
        print(time_remaining)
        time.sleep(1)
        seconds -= 1
    messagebox.showinfo("Focus Timer", "Time up! Take a break.")

# 设置专注时长为25分钟
focus_minutes = 25
start_focus_timer(focus_minutes)
