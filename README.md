# Machine Learning Powered Voice Assistant
This is a machine learning powered and speech-based virtual assistant specifically designed for Raspberry Pi.

# Currently supported features (more to be added soon)
* Basic conversation (greetings, questions, etc.)
* Geolocation
* Weather (temperature, humidity, etc.) based on current location
* Date/time features (day, month, year, etc.)
* Opening websites (Google, GitHub, Wikipedia, etc.) in the browser
* Creating, pausing, and deleting timers. Timers run in the background so the program does not wait for the timer to end before listening for more input.
* Repeating a certain phrase a specified number of times.
* Exiting on command

# How to run code
* Download code in a directory called assistant
* Navigate to the directory in terminal/command prompt: `cd assistant/`
* Install the required python packages: `pip install -r requirements.txt`
* Get porcupine API access key (explained in next section)
* Run main.py : `python main.py`

# How to add `access_key` to line 60 in `main.py`
* Go to https://picovoice.ai/platform/porcupine/
* Create a account and then grab your API key
* Paste your API key and DO NOT share it! :)

# How the assistant works
The following steps give a brief overview on how the assistant works:
* The program continously listens for a user to say the wake word (currently set to "Jarvis"). 
* When a wake word is detected, the program uses speech recognition to determine what the user says. 
* The `IntentClassifier` class (found in `/intentclassifier/intent_classification.py`) classifies the user's intent using the Support Vector Machine (SVM) algorithm that trains on a dataset containing sample user prompts along with their intent.
* Based on the classified intent, the assistant executes the correct function. This function is found in the `/assistant_functions` directory. This structure makes it easy to add new functionality to the assistant.
* For more details on these functions' implementations, see the `/assistant_functions` directory.
