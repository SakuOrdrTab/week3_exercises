import os

from transformers import pipeline
from groq import Groq

class Analyzer():
    def __init__(self):
        self._custom_model = None
        hf_token = os.getenv("HF_HUB_TOKEN")
        model_name = "kelmeilia/wk3ex_bert_imdb_sentiment"  
        self._classifier = pipeline("text-classification", model=model_name, token=hf_token)
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
            prediction = self._classifier(text)
            # print(prediction)
            confidence = prediction[0]["score"]
            if prediction[0]["label"] == "LABEL_1":
                sentiment = "positive"
            elif prediction[0]["label"] == "LABEL_0":
                sentiment = "negative"
            else:
                raise ValueError("Model did a crazy value!")
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
