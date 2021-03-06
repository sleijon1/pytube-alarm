import tkinter as tk
from tkinter import messagebox
from alarm import Alarm
from time import sleep
import threading

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.initiate_main_gui()
        self.initiate_tk_window()
        self.window.mainloop()
    
    def initiate_main_gui(self):
        """ initiates gui objects ready to be placed """
        self.minutes_entry = tk.Entry(master=self.window)
        self.seconds_entry = tk.Entry(master=self.window)
        self.url_entry = tk.Entry(master=self.window)
        self.url_label = tk.Label(
            master=self.window,
            text="url to open when time is up",
            fg="black",
        )
        self.minutes_label = tk.Label(
            master=self.window,
            text="Minutes",
            fg="black",
        )
        self.seconds_label = tk.Label(
            master=self.window,
            text="Seconds",
            fg="black",
        )
        self.button = tk.Button(
            master=self.window,
            text="Set Alarm",
            bg="green",
            fg="yellow",
            relief=tk.RAISED,
            command=self.user_submit,
        )

    def initiate_time_window(self):
        self.time_window = tk.Toplevel(self.window)
        self.time_left_label = tk.Label(
            master=self.time_window,
            text="Hello, Tkinter",
            fg="blue",
            bg="black",
            font=("Courier", 35)
        )
        self.time_left_label.pack(fill=tk.BOTH)

    def initiate_tk_window(self):
        """ places gui objects on grid and starts tk window loop """
        self.minutes_entry.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        self.minutes_label.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        self.seconds_entry.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')
        self.seconds_label.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        self.url_label.grid(row=2, column=0, padx=5, pady=5, columnspan=2, sticky='ew')
        self.url_entry.grid(row=3, column=0, padx=5, pady=5, columnspan=2, sticky='ew')

        self.button.grid(row=4, column=0, padx=2, pady=2, columnspan=2, sticky='ew')

        self.window.columnconfigure([0, 1], weight=1, minsize=50)
        self.window.rowconfigure([0, 1, 2, 3], weight=1, minsize=20)

    def user_submit(self):
        """ receive user input and check that its reasonable giving user feedback
        via prompts """
        minutes = self.minutes_entry.get()
        seconds = self.seconds_entry.get()
        url = self.url_entry.get()

        confirm_url = None
        no_integer_error = False
        no_input_error = False
        weird_url_warning = False

        if minutes == '' and seconds == '':
            print('we chilling')
            no_input_error = True
        else:
            try:
                minutes = int(minutes) if minutes != '' else 0
                seconds = int(seconds) if seconds != '' else 0 
            except ValueError:
                no_integer_error = True
        if 'youtube' not in url:
            weird_url_warning = True

        if no_input_error:
            messagebox.showerror(title='InputError', message='How can your alarm go off in 0 seconds and 0 minutes? Are you some sort of time bender?')
            return
        elif no_integer_error:
            messagebox.showerror(title='TypeError', message='Please use numbers for your alarm. I don\'t speak jibberish.')
            return
        elif weird_url_warning:
            confirm_url = messagebox.askquestion(title='WeirdUrlDude', message='Are you sure your alarm is suppose to be this weird url?')
        
        if confirm_url == 'yes' or confirm_url is None:
            alarm = Alarm(minutes=minutes, seconds=seconds)
            self.window.withdraw()
            self.initiate_time_window()
            alarm_thread = threading.Thread(target=alarm.start_timer, args=(self, url,))
            alarm_thread.start()
        else:
            return
    
    def update_time(self, time_left, minutes=False):
        if time_left <= 0:
            self.time_left_label["text"] = '0'
            self.time_window.destroy()
            self.window.deiconify()
        else:
            # set time left
            if minutes == True:
                self.time_left_label["text"] = str(time_left) + " min"
            else:
                self.time_left_label["text"] = str(time_left)



if __name__ == '__main__':
    gui = GUI()