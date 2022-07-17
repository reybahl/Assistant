from assistant_functions.TimerEvent import TimerEvent
import time
from assistant_functions.determine_most_similar import determine_most_similar_phrase
from word2number import w2n
from assistant_functions.speak_listen import speak_listen

class Timer:
    """
    Class that handles all the created TimerEvent objects
    """
    def __init__(self):
        self.timers = []
    
    def main(self, text:str, intent:str):
        action = self.classify_action(text)
        prompt = ""
        function = None
        if action == 'add':
            prompt = "For how many seconds should I set the timer?"
            function = self.add_timer
        elif action == 'pause':
            prompt = "State the number of the timer I should stop."
            function = self.pause_timer
        elif action == 'continue':
            prompt = "Enter the number of the timer I should continue."
            function = self.resume_timer
        elif action == 'delete':
            prompt = "Enter the number of the timer I should delete."
            function = self.delete_timer

        num = -1
        while num == -1:
            try:
                num = w2n.word_to_num(text)
                break
            except:
                for tok in text.split():
                    if tok.isdigit():
                        num = int(tok)
                        break
                if num != -1:
                    break

            speak_listen.say(prompt)
            text = speak_listen.listen()
        
        # execute the correct function, set at the beginning of this function
        function(num)

    def classify_action(self, text:str):
        phrases = {
            'start timer' : 'add',
            'new timer' : 'add',
            'add timer': 'add',
            'stop timer': 'pause',
            'pause timer': 'pause',
            'continue timer' : 'resume',
            'resume timer': 'resume',
            'delete timer': 'delete',
            'cancel timer': 'delete'
        }

        most_similar = determine_most_similar_phrase(text, phrases)
        return phrases[most_similar]

    def add_timer(self, seconds):
        self.timers.append(TimerEvent(seconds))
        self.timers[len(self.timers)-1].start()
        speak_listen.say(f"Your timer for {seconds} seconds started now")
    
    def pause_timer(self, index):
        """Pauses the timer at the specified index"""
        if index <= len(self.timers):
            self.timers[index-1].pause()
            speak_listen.say(f"Your timer {index} is now paused.")

        speak_listen.say(f"You only have {len(self.timers)} timers")
    
    def resume_timer (self, index):
        """continues a paused timer"""
        if index <= len(self.timers):
            self.timers[index-1].start()
    
    def delete_timer(self, index):
        """deletes a timer"""
        if index <= len(self.timers):
            # pause it
            self.timers[index-1].pause()
            # remove its reference
            del self.timers[index-1]

timer = Timer()