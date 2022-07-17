# Machine Learning Powered Voice Assistant
This is a machine learning powered and speech-based virtual assistant specifically designed for Raspberry Pi.

# Currently supported features (more to be added soon)
* Basic conversation (greetings, questions, etc.)
* Geolocation
* Weather (temperature, humidity, etc.) based on current location
* Date/time features (day, month, year, etc.)
* Opening websites (Google, GitHub, Wikipedia, etc.) in the browser
* Creating, pausing, and deleting timers. Timers run in the background so the program does not wait for the timer to end before listening for more input.

# How to run code
* Download code in a directory called assistant
* Navigate to the directory in terminal/command prompt: `cd assistant/`
* Install the required python packages: `pip install -r requirements.txt`
* Run main.py : `python main.py`

# How the assistant works
The program continously listens for a user to say the wake word (currently set to "Jarvis"). Then, the program uses speech recognition to determine the user's input.
