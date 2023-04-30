import flask
import datahandle

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Test</h1><p>This site is a prototype API for receiving data from the Arduino.</p>"

@app.route('/api/v1/data', methods=['POST', 'GET'])
def get_data():
    if flask.request.method == 'POST':
        data = flask.request.data
        print(data)
        datahandle.manage_data(data)
        return "Data received"
    else:
        print("No data received")
        return "No data received"
    


app.run(host='0.0.0.0', port=5000)