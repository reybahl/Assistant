import time
import threading

class TimerEvent:
    def __init__(self, seconds:int):
        """
        time = time in seconds
        """
        self.seconds = seconds
        
    def start(self):
        self.status = True # stores whether or not to continue the timer
        self.timer_thread = threading.Thread(target=self.countdown)
        self.timer_thread.start()
    
    def pause(self):
        self.status = False

    def countdown(self):
        while (self.status and self.seconds):
            self.seconds -= 1
            time.sleep(1)

        # if the time is zero
        if (not self.seconds):
            print("timer over")

    

# testing
if __name__ == "__main__":
    x = TimerEvent(10)
    x.start()
    print("other stuff")
    x.stop()