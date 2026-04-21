import tkinter as tk
import requests
import time

PI_URL = "http://192.168.240.123:5000/status"

root = tk.Tk()
root.title("messagebox")
root.geometry("300x150")
root.withdraw()  # hide first

label = tk.Label(root, text="We are not alone! ")
label.pack(expand=True)

def check_popup():
    try:
        data = requests.get(PI_URL, timeout=1).json()
        if data.get("should_popup"):
            root.deiconify()  # show
        else:
            root.withdraw()  # hide
    except:
        pass
    root.after(500, check_popup)  # checks every 500milisec

check_popup()
root.mainloop()
