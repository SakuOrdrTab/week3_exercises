import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from analyzer import Analyzer

app = Flask(__name__)

CORS(app)

@app.route('/analyze/', methods=['POST'])
def analyze():
    data = request.json
    text = data.get("text", "").strip()
    model = data.get("model", "custom").lower()
    
    if not text:
        return jsonify({"error": "Text parameter is required"}), 400
    if model not in {"custom", "llama"}:
        return jsonify({"error": "Invalid model specified"}), 400

    sentiment, conf = analyzer.predict(text, model)      
    return jsonify({"sentiment": sentiment, "confidence" : conf})

if __name__ == '__main__':
    analyzer = Analyzer()
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, port=port)