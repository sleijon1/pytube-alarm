from datetime import datetime, timedelta
from playsound import playsound
import webbrowser

class Alarm:
    """ alarm class """
    timer_hours = None
    timer_minutes = None
    timer_seconds = None

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.timer_hours = hours
        self.timer_minutes = minutes
        self.timer_seconds = seconds

    def start_timer(self, url=None):
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
            print(datetime.now().replace(microsecond=0), end_time)
            # misses equality since it loops too slowly
            if datetime.now().replace(microsecond=0) == end_time:
                if url is None:
                    playsound('default.mp3')
                else:
                    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:/Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                    webbrowser.get('chrome').open_new(url)
                break


#alarm = Alarm(seconds=2)
#alarm.start_timer('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')
