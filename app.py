from flask import Flask, request
import requests
from flask import jsonify
from os import listdir
from os.path import isfile, join
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
def main(argv):
    global devices

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route("/devices")
def getDevices(): 
    global devices
    devices = []
    mypath = "./devices"
    device_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    i = 0
    for filename in device_files: 
        print(join(mypath, filename))
        f = open(join(mypath, filename), "r")
        devices.append(json.loads(f.read()))
        
    return jsonify(devices)
@app.route('/devices/<section>')
def coffeState(section):
    global devices
    deviceName = request.view_args['section']
    print(deviceName)
    URL = "http://"
    
    for i in devices:
        if (i.get('name') == deviceName):
            URL = 'http://' + i.get('ip')
    if (request.args.get('set') == None): 

        
        r = requests.get(url = URL)
        data = r.json()

        print(r.json())
        return jsonify(data)

    else: 
        state = int(request.args.get('set'))
        URL = URL + "?set=" + str(state)
        r = requests.get(url = URL)
        data = r.json()
        print(r.json())
        return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
