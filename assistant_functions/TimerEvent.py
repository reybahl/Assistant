import time
import threading

class TimerEvent:
    def __init__(self, time):
        """
        time = time in seconds
        """
        self.time = time
        self.status = True # stores whether or not to continue the timer
        
    def start(self):
        self.timer_thread = threading.Thread(target=self.countdown)
        self.timer_thread.start()
    
    def stop(self):    
        self.status = False

    def countdown(self):
        while (self.status and self.time):
            self.time -= 1
            time.sleep(1)

        # if the time is zero
        if (not self.time):
            print("timer over")

    


x = TimerEvent(10)
x.start()
print("other stuff")
x.stop()