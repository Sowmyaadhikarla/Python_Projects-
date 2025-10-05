from time import strftime
import tkinter as tk

root = tk.Tk()
root.title("Digital Clock")
root.configure(bg="black")
root.geometry("500x200")

time_label=tk.Label(root,font=("ds_digital",60,"bold"),background="black",foreground="cyan")
time_label.pack(anchor="center")

data_label=tk.Label(root,font=("Arial",20,"bold"),background="black",foreground="white")
data_label.pack(anchor="s")

def update_time():
    current_time=strftime("%H:%M:%S %p")
    current_date=strftime("%A:%B %d:%Y")
    time_label.config(text=current_time)
    data_label.config(text=current_date)
    time_label.after(1000,update_time)

update_time()
root.mainloop()