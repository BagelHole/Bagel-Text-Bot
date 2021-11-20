# text bot
import sys
import tkinter as tk
from time import sleep
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import pyautogui

bg_color = "#2f3136"
highlight_color = "#5865F2" 
accent_color = "#929bf6"

def auto_type(user_times,user_text,repeating_var,interval_ks_var,interval_ks_text,interval_mes_var,interval_mes_text,check_return_var):
    user_times_out = user_times.get()
    user_text_out = user_text.get()
    interval_ks_text_out = interval_ks_text.get()
    interval_mes_text_out = interval_mes_text.get()

    interval_ks_speed = 0.15
    interval_mes_speed = 0

    if interval_ks_var == 1:
        while True:
            try:
                interval_ks_speed = float(interval_ks_text_out)
                break
            except:
                tk.messagebox.showwarning(title=None, message="Input a Key Stroke Interval Time")
                return

    if interval_mes_var == 1:
        while True:
            try:
                interval_mes_speed = int(interval_mes_text_out)
                break
            except:
                tk.messagebox.showwarning(title=None, message="Input a Message Interval Time")
                return

    if repeating_var == 0:
        while True:
            try: 
                user_times_out = int(user_times_out)
                break
            except:
                tk.messagebox.showwarning(title=None, message="Input a Number for Times to Write")
                return

        for x in range(user_times_out):
            label_running.pack()
            root.update()
            if x == 0:
                sleep(5)
            else:
                if interval_mes_var == 1:
                    interval_mes_speed_count = interval_mes_speed
                    for x in range(interval_mes_speed):
                        mins, secs = divmod(interval_mes_speed_count, 60)
                        timeformat = '{:02d}:{:02d}'.format(mins, secs)
                        speed_out = (timeformat)
                        time_message_label.config(text=speed_out,font=("",18,),fg="white",bg=bg_color)
                        time_until_label.pack()
                        time_message_label.pack()
                        root.update()
                        sleep(1)
                        interval_mes_speed_count -= 1
                else:
                    sleep(interval_mes_speed)
            pyautogui.write(user_text_out, interval=interval_ks_speed)
            if check_return_var == 1:
                pyautogui.press("enter")
        else:
            time_message_label.pack_forget()
            time_until_label.pack_forget()
            label_running.pack_forget()

    elif repeating_var == 1: 
        for x in range(sys.maxsize**10):
            label_running.pack()
            root.update()
            if x == 0:
                sleep(5)
            else:
                if interval_mes_var == 1:
                    interval_mes_speed_count = interval_mes_speed
                    for x in range(interval_mes_speed):
                        mins, secs = divmod(interval_mes_speed_count, 60)
                        timeformat = '{:02d}:{:02d}'.format(mins, secs)
                        speed_out = (timeformat)
                        time_message_label.config(text=speed_out,font=("",18,),fg="white",bg=bg_color)
                        time_until_label.pack()
                        time_message_label.pack()
                        root.update()
                        sleep(1)
                        interval_mes_speed_count -= 1
                else:
                    sleep(interval_mes_speed)
            pyautogui.write(user_text_out, interval=interval_ks_speed)
            if check_return_var == 1:
                pyautogui.press("enter")
        else:
            label_running.pack_forget()
            time_message_label.pack_forget()
            time_until_label.pack_forget()

def repeat_button(repeating_var):
    if repeating_var == 1:    
        times_input.delete(0, last=None)
        times_input.configure(state="disabled")
    elif repeating_var == 0:
        times_input.configure(state="normal")

def interval_ks_button(interval_var):
    if interval_var == 1:
        interval_ks_label.pack()
        interval_ks_input.pack()
    elif interval_var == 0:
        interval_ks_label.pack_forget()
        interval_ks_input.pack_forget()

def interval_mes_button(interval_var):
    if interval_var == 1:
        interval_mes_label.pack()
        interval_mes_input.pack()
    elif interval_var == 0:
        interval_mes_label.pack_forget()
        interval_mes_input.pack_forget()

def stop_button_func():
    label_running.pack_forget()
    time_message_label.pack_forget()
    time_until_label.pack_forget()
    label_stopping.pack()
    root.update()
    sleep(1)
    label_stopping.pack_forget()
    root.quit()
    app.mainloop()

def check_return_button(interval_var):
    return

# GUI
root = tk.Tk()
root.title("Bagel Text Bot")
repeating_var = tk.IntVar(0)
interval_ks_var = tk.IntVar(0)
interval_mes_var = tk.IntVar(0)
check_return_var = tk.IntVar(0)
helv36 = font.Font(family='courier', size=20, weight='bold')

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        root.geometry("600x600")
        root.configure(bg=bg_color)

        label_text = tk.Label(root, text="Text to Write: ")
        label_text.config(font=("",24,),fg="white",bg=bg_color)

        label_times = tk.Label(root, text="How Many Times to Write: ")
        label_times.config(font=("",18),fg="white",bg=bg_color)

        label_info = tk.Label(root, text="You have 5 seconds to click where you want the text to write.")
        label_info.config(font=("Courier", 14),fg=accent_color,bg=bg_color)

        user_text = tk.StringVar()
        text_input = tk.Entry(root, textvariable=user_text,width=60)
        text_input.configure(bd=1,highlightcolor=highlight_color)
        text_input.focus() 
    
        text_button = Button(master = root, command = lambda: auto_type(times_text,user_text,repeating_var.get(),interval_ks_var.get(),interval_ks_text,interval_mes_var.get(),interval_mes_text,check_return_var.get()),height = 2, width = 8,text = "Start",font=helv36,fg="#10a43e")

        stop_button = Button(master = root, command = lambda: stop_button_func(),height = 2, width = 8,text = "Stop",font=helv36,fg="red")

        root.bind('<Return>', lambda x: auto_type(times_text,user_text,repeating_var.get(),interval_ks_var.get(),interval_ks_text,interval_mes_var.get(),interval_mes_text,check_return_var.get()))
        root.bind("<Escape>", lambda x: stop_button_func())

        check_repeat = Checkbutton(root, text="Repeating?", variable=repeating_var, command=lambda: repeat_button(repeating_var.get()))
        check_repeat.config(font=("",18),fg="white",bg=bg_color)

        check_interval_ks = Checkbutton(root, text="Change Key Stroke Interval? (default: 0.15s)", variable=interval_ks_var, command=lambda: interval_ks_button(interval_ks_var.get()))
        check_interval_ks.config(font=("",18),fg="white",bg=bg_color)

        check_interval_mes = Checkbutton(root, text="Change Message Interval? (default: 0s)", variable=interval_mes_var, command=lambda: interval_mes_button(interval_mes_var.get()))
        check_interval_mes.config(font=("",18),fg="white",bg=bg_color)

        check_return = Checkbutton(root, text="Add a Enter/Return after message?", variable=check_return_var, command=lambda: check_return_button(check_return_var.get()))
        check_return.config(font=("",18),fg="white",bg=bg_color)

        label_text.pack()
        text_input.pack()

        label_times.pack()
        times_input.pack()
        check_repeat.pack()

        text_button.pack(ipadx=30)
        stop_button.pack(pady=10,ipadx=30)
        label_info.pack()

        check_return.pack()
        check_interval_ks.pack()
        check_interval_mes.pack()

        new_tab_order=[text_input,times_input,text_button,stop_button]
        for widget in new_tab_order:
            widget.lift()
        
label_running = tk.Label(root, text="◉  Running  ◉")
label_running.config(font=("",48,),fg="#57F287",bg=bg_color)

label_stopping = tk.Label(root, text="▣  Stopping  ▣")
label_stopping.config(font=("",48,),fg="red",bg=bg_color)

time_message_label = tk.Label(root,text="")

time_until_label = tk.Label(root, text="Next Message In:")
time_until_label.config(font=("",18,),fg=accent_color,bg=bg_color)

times_text = tk.StringVar()
times_input = tk.Entry(root, textvariable=times_text)
times_input.configure(bd=1,highlightcolor=highlight_color)

interval_ks_text = tk.StringVar()
interval_ks_input = tk.Entry(root, textvariable=interval_ks_text)
interval_ks_input.configure(bd=1,highlightcolor=highlight_color)

interval_ks_label = tk.Label(root,text="What interval of time between key strokes? (Seconds):")
interval_ks_label.config(font=("",18,),fg="white",bg=bg_color)

interval_mes_text = tk.StringVar()
interval_mes_input = tk.Entry(root, textvariable=interval_mes_text)
interval_mes_input.configure(bd=1,highlightcolor=highlight_color)

interval_mes_label = tk.Label(root,text="What interval of time between messages? (Seconds):")
interval_mes_label.config(font=("",18,),fg="white",bg=bg_color)

app = Application(master=root)
app.mainloop()
