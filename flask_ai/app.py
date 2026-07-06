from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    # 這裡可實作對應的 AI 邏輯或讀取 faq.json
    return jsonify({"reply": f"這是針對 '{user_message}' 的 AI 自動回覆。"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
