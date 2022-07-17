import webbrowser
from assistant_functions.determine_most_similar import determine_most_similar_phrase
from assistant_functions.speak_listen import speak_listen
import re


class AssistantBrowser():
    def main(self, text, intent):
        task = self.determine_search_or_open(text)
        if task == 'open':
            self.open(text)
        elif task == 'search':
            self.extract_search_term_and_website(text)

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
            'kahoot' : 'https://kahoot.it/',
            'github' : 'https://github.com/',
            'news' : 'https://news.google.com' 
        }
        speak_listen.say("Sure!")
        text= text.lower()
        for website_name, web_address in websites.items():
            if website_name in text:
                webbrowser.open(web_address)
    
    def extract_search_term_and_website(self, text):
        text = text.lower()
        text = text.replace("search for", "search")
        
        list_of_websites_to_search = ['google', 'wikipedia', "github"]
        website_to_search = None
        for website in list_of_websites_to_search:
            if website in text:
                website_to_search = website
                text = text.replace(f"on {website}", "")
                text = text.replace(f"{website} for", "")
                break
        
        x = re.search("(?<=search).*$", text)
        search_term = x.group().strip()
        
        if website_to_search is not None and search_term is not None:
            self.search_and_open(website_to_search, search_term)
        
    def search_and_open(self, website, search_term):
        speak_listen.say("Sure!")
        urls_to_search_dict = {
            'google' : 'https://www.google.com/search?q={}',
            'wikipedia' : 'https://en.wikipedia.org/wiki/Special:Search/{}',
            'github' : "https://github.com/search?q={}"
        }
        search_url = urls_to_search_dict[website]
        url_to_open = search_url.replace("{}", search_term)
        webbrowser.open(url_to_open)

assistant_browser = AssistantBrowser()
