import tkinter as tk
from tkinter import messagebox


class GUI:
    window = None
    minutes_entry = None
    seconds_entry = None
    url_entry = None
    url_label = None
    minutes_label = None
    seconds_label = None
    button = None
    
    def __init__(self):
        self.window = tk.Tk()
        self.minutes_entry = tk.Entry(master=self.window)
        self.seconds_entry = tk.Entry(master=self.window)
        self.url_entry = tk.Entry(master=self.window)
        self.url_label = tk.Label(
            master=self.window,
            text="url to open",
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

    def initiate_tk_window(self):
        self.minutes_entry.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        self.minutes_label.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        self.seconds_entry.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')
        self.seconds_label.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        self.url_label.grid(row=2, column=0, padx=5, pady=5, columnspan=2, sticky='ew')
        self.url_entry.grid(row=3, column=0, padx=5, pady=5, columnspan=2, sticky='ew')

        self.button.grid(row=4, column=0, padx=2, pady=2, columnspan=2, sticky='ew')

        self.window.columnconfigure([0, 1], weight=1, minsize=50)
        self.window.rowconfigure([0, 1, 2, 3], weight=1, minsize=20)

        self.window.mainloop()

    def user_submit(self):
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
                minutes = int(minutes)
                seconds = int(seconds)
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
            # run backend
            pass
        else:
            return
        print(minutes, seconds, url)    

gui = GUI()
gui.initiate_tk_window()