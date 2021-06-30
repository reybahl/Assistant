import webbrowser
from assistant_functions.determine_most_similar import determine_most_similar_phrase
from assistant_functions.speak_listen import speak_listen

class AssistantBrowser():
    def main(self, text, intent):
        task = self.determine_search_or_open(text)
        if task == 'open':
            self.open(text)
        elif task == 'search':
            self.search(text)

    def determine_search_or_open(self, text):
        phrases = {
            'open and search' : 'search',
            'open' : 'open',
            'search' : 'search',
            'open in browser' : 'open' 
        }

        most_similar = determine_most_similar_phrase(text, phrases)
        return phrases[most_similar]
    def open(self, text):
        websites = {
            'google' : 'https://www.google.com',
            'wikipedia' : 'https://en.wikipedia.org/',
            'kahoot' : 'http://kahoot.it/'
        }
        speak_listen.say("Sure!")
        text= text.lower()
        for website_name, web_address in websites.items():
            if website_name in text:
                webbrowser.open(web_address)

assistant_browser = AssistantBrowser()