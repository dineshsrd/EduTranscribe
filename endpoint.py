from flask import Flask, redirect, url_for, request, jsonify
import json

from extractor import extract
from summary import summaryAndKeyword
from flask_cors import CORS 


app = Flask(__name__)
CORS(app) 


@app.route('/api/v1/translate', methods=['POST'])
def translate():
    data = request.json
    result = extract(data["video_url"])
    return jsonify(result)

@app.route('/api/v1/generate/summary_keywords', methods=['POST'])
def summary():
    data = request.json
    result = summaryAndKeyword(data["transcript"])
    return jsonify(result)

@app.route('/api/v1/generate/keywords', methods=['POST'])
def keywords():
    data = request.json
    return jsonify(data)

@app.route('/api/v1/generate/keyword_summary', methods=['POST'])
def keywordSummary():
    data = request.json
    return jsonify(data)










@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)