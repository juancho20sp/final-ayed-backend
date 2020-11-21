from flask import Flask


app = Flask(__name__)

# Damos el endpoint
@app.route('/api', methods=['GET'])

def api():
    return {
        'userID': 1,
        'title': 'Flask React Application',
        'completed': False
    }