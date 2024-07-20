from transformers import pipeline

class IntentClassifier:
    
    def __init__(self, model, categories) -> None:
        self.pipe = pipeline(model=model)
        self.categories = categories

    def classify(self, input):
        return self.pipe(input, candidate_labels=self.categories)

pipe = "facebook/bart-large-mnli"
categories = ["greeting", "leaving", "news", "timer", "weather", "compliment", "insult", "personal question", "open in browser", "date", "time", "repeat", "timer"]

classifier = IntentClassifier(pipe, categories)
print(classifier.classify(input("enter text: ")))