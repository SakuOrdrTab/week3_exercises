import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def wrap_prompt(text : str) -> str:
    return [
        {
            "role" : "user",
            "content" : f"Estimate the following text and answer in just one word, 'positive', \
                or 'negative' if the sentiment of the text is of positive or negative sentiment.\n\
                text: {text}"
        }
    ]

chat_completion = client.chat.completions.create(
    messages=wrap_prompt("Gone with the wind was mediocre"),
    model="llama-3.3-70b-versatile",
)

answer = chat_completion.choices[0].message.content
print(f"Positive in answer {'positive' in answer.lower()}")
print(f"Negative in answer {'negative' in answer.lower()}")
print("Answer: ", answer)

from huggingface_hub import HfApi

api = HfApi()
model_info = api.model_info("kelmeilia/wk3ex_bert_imdb_sentiment")

print(model_info)