from datetime import datetime, timedelta
from playsound import playsound
import webbrowser
from time import sleep
from math import floor

class Alarm:
    """ alarm class """
    timer_hours = None
    timer_minutes = None
    timer_seconds = None

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.timer_hours = hours
        self.timer_minutes = minutes
        self.timer_seconds = seconds

    def start_timer(self, gui, url=None):
        """ Starts timer using timer_minutes
        url -- either local path to mp3 or youtube link
        """
        start_time = datetime.now()
        delta = timedelta(
                          hours=self.timer_hours,
                          minutes=self.timer_minutes,
                          seconds=self.timer_seconds
                        )
        end_time = start_time + delta
        end_time = end_time.replace(microsecond=0)
        while True:
            time_delta_left = (end_time - datetime.now().replace(microsecond=0)).seconds
            minutes_left = floor((time_delta_left-30)/60)
            if minutes_left > 1:
                gui.update_time(minutes_left, minutes=True)
                sleep(30)
            else:
                gui.update_time(time_delta_left)
                sleep(1)
            if time_delta_left <= 0:
                if url is None:
                    playsound('default.mp3')
                else:
                    webbrowser.get().open_new(url)
                break
