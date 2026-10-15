from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"status": "ok", "pid": os.getpid()})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/compute')
def compute():
    total = 0
    for i in range(50000):
        total += i * i
    return jsonify({"result": total, "pid": os.getpid()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)