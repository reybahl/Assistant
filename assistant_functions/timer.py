from TimerEvent import TimerEvent
import time

class Timer:
    """
    Class that handles all the created TimerEvent objects
    """
    def __init__(self):
        self.timers = []

    def add_timer(self, seconds):
        self.timers.append(TimerEvent(seconds))
        self.timers[len(self.timers)-1].start()
    
    def pause_timer(self, index):
        """Pauses the timer at the specified index"""
        if index < len(self.timers):
            self.timers[index].pause()
    
    def resume_timer (self, index):
        """continues a paused timer"""
        if index < len(self.timers):
            self.timers[index].start()
    
    def delete_timer(self, index):
        """deletes a timer"""
        if index < len(self.timers):
            # pause it
            self.timers[index].pause()
            # remove its reference
            del self.timers[index]

# testing
if __name__ == "__main__":
    timer = Timer()
    timer.add_timer(10)
    timer.add_timer(10)
    timer.add_timer(15)
    timer.pause_timer(0)
    timer.delete_timer(1)
    print("pausing first timer for 5 seconds")
    time.sleep(5)
    timer.resume_timer(0)