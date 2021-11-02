from datetime import datetime, timedelta
from playsound import playsound

class Alarm:
    """ alarm class """
    timer_hours = None
    timer_minutes = None
    timer_seconds = None
    play_youtube = False

    def __init__(self, hours=0, minutes=0, seconds=0, youtube=False):
        self.timer_hours = hours
        self.timer_minutes = minutes
        self.timer_seconds = seconds
        self.play_youtube = youtube

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
            # misses equality since it loops too slowly
            if datetime.now().replace(microsecond=0) == end_time:
                if not self.play_youtube:
                    playsound('default.mp3')
                else:
                    # play youtube link by opening browser or
                    # download it and name it and play from file
                    youtube_url = url
                    pass



alarm = Alarm(seconds=5)
alarm.start_timer()
