
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import MethodNotAllowed

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/', strict_slashes=False)
def hello_world():
    if request.method == "GET":
        new_dict = {
            'slackUsername': 'TommyOnCode',
            'backend': True,
            'age': 21,
            'bio': "I'm a Software Engineer, with intermediary knowledge of python"
            }
        return jsonify(new_dict)
    else:
        raise MethodNotAllowed(['GET'])

