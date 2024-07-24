class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __repr__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def format_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def sum_times(self, t2):
        """return the result by using sum_times() method"""

        seconds = self.seconds + t2.seconds
        minutes = self.minutes + t2.minutes + seconds // 60
        hours = self.hours + t2.hours + minutes // 60
        seconds %= 60
        minutes %= 60
        return Time(hours, minutes, seconds)

    def __add__(self, t2):
        """return the result by using sum_times() method"""

        seconds = self.seconds + t2.seconds
        minutes = self.minutes + t2.minutes + seconds // 60
        hours = self.hours + t2.hours + minutes // 60
        seconds %= 60
        minutes %= 60
        return Time(hours, minutes, seconds)
