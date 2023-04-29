import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Test</h1><p>This site is a prototype API for receiving data from the Arduino.</p>"

@app.route('/api/v1/data', methods=['POST'])
def get_data():
    data = flask.request.json
    print(data)
    return "OK"

app.run(host='0.0.0.0', port=5000)