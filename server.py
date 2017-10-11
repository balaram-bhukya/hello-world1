from flask import Flask, request, jsonify
from matcher import mapper
import os

app = Flask(__name__)


@app.route('/matcher', methods=['POST'])
def matcher():
    content = request.get_json(silent=True)
    
    return jsonify(mapper(content['sentence'], content['intents']))


if __name__ == "__main__":
    app.run(debug=True)
    app.run(port=5008)
    # port = int(os.environ.get('PORT', 8000))
    # # app.run(host='0.0.0.0', port=port)
    # app.run(host='127.0.0.1', port=port)

