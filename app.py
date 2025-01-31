from flask import Flask, request, jsonify

app = Flask(__name__)

def analyze_sentiment_custom(text):
    """Simple rule-based sentiment analysis."""
    positive_words = {"good", "happy", "great", "excellent", "awesome"}
    negative_words = {"bad", "sad", "terrible", "awful", "worst"}
    
    words = set(text.lower().split())
    if words & positive_words:
        return "positive"
    elif words & negative_words:
        return "negative"
    return "neutral"

def analyze_sentiment_llama(text):
    """Placeholder function for Llama-based sentiment analysis."""
    return "positive" if "good" in text.lower() else "negative"

@app.route('/analyze/', methods=['POST'])
def analyze():
    data = request.json
    text = data.get("text", "").strip()
    model = data.get("model", "custom").lower()
    
    if not text:
        return jsonify({"error": "Text parameter is required"}), 400
    if model not in {"custom", "llama"}:
        return jsonify({"error": "Invalid model specified"}), 400
    
    if model == "custom":
        sentiment = analyze_sentiment_custom(text)
    else:
        sentiment = analyze_sentiment_llama(text)
    
    return jsonify({"sentiment": sentiment})

if __name__ == '__main__':
    import os
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, port=port)