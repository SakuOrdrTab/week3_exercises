import os

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from analyzer import Analyzer

app = Flask(__name__, static_folder="dist", static_url_path="/")

CORS(app)

# Serve the React frontend
@app.route('/')
@app.route('/<path:path>')
def serve_frontend(path="index.html"):
    return send_from_directory(app.static_folder, path)

# Serve sentiment analysis
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