from assistant_functions.speak_listen import speak_listen
import random
from word2number import w2n

class Repeat:
    def repeat(self, input_text, intent):
        count = 1
        input_text.replace("once", '1')
        input_text.replace("twice", '2')
        input_text.replace("thrice", '3')
        try:
            count = w2n.word_to_num(input_text)
        except:
            for tok in input_text.split():
                if tok.isdigit():
                    count = int(tok)
                    break

        speak_listen.say(random.choice(["What should I repeat?", "What do you want me to say?"]))
        repeat_text = speak_listen.listen()

        for x in range(count):
            speak_listen.say(repeat_text + " ")

repeat = Repeat()