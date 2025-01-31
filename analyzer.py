import os

from transformers import pipeline
from groq import Groq

class Analyzer():
    def __init__(self):
        self._custom_model = None
        model_name = "kelmeilia/results"  
        self._classifier = pipeline("text-classification", model=model_name)
        self._client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    def wrap_prompt(self, text : str) -> str:
        return [
            {
                "role" : "user",
                "content" : f"Estimate the following text and answer in just one word, 'positive', \
                or 'negative' if the sentiment of the text is of positive or negative sentiment.\n\
                text: {text}"
            }
        ]

    def predict(self, text : str, model : str) -> tuple:
        if model == "custom":
            sentiment, confidence = self._classifier(text)
        elif model == "llama":
            print("Need to use Groq")
            chat_completion = self._client.chat.completions.create(
                messages=self.wrap_prompt(text),
                model="llama-3.3-70b-versatile",
            )
            response = chat_completion.choices[0].message.content
            print(f"Chat completion:\n{response}")
            if "positive" in response.lower():
                sentiment = "positive"
            elif "negative" in response.lower():
                sentiment = "negative"
            confidence = 0.5
        else:
            print("No model was asked in Analyzer.predict()!")
            sentiment, confidence = None, None
        return sentiment, confidence
    
if __name__ == "__main__":
    analyzer = Analyzer()
    print(analyzer.predict("I really loved this movie!", "custom"))
