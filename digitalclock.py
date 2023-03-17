import tkinter as tk

from datetime import datetime

root = tk.Tk()
root.title("Digital Clock")

def clock():
    now = datetime.now()
    timelabeled = ("%s/%s/%s   %s:%s:%s" % (now.day, now.month, now.year, now.hour, now.minute, now.second))
    w.config(text = timelabeled, )
    root.after(1000,clock)

w = tk.Label(font = (100))
w.pack()
clock()
root.mainloop()