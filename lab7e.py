import datetime

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return self.format_time()

    def __repr__(self):
        return self.format_time()

    def format_time(self):
        time = datetime.time(hour=self.hours, minute=self.minutes, second=self.seconds)
        return time.strftime('%H:%M:%S')
