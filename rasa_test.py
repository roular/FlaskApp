import json
import requests
from flask import Flask,request
app = Flask(__name__)

######POST request
@app.route('/get_intent_name', methods=["POST"])
def index():
    url = 'http://localhost:5005/model/parse/'
    msg= request.get_json()['msg']
    payload = {
        "text": msg
    }
    x = requests.post(url, json=payload)
    y = json.loads(x.text)
    print(x.text)
    return y["intent"]['name']

    ####GET request
# @app.route('/get_intent_name/<text>')
# def index(text):
#     url = 'http://localhost:5005/model/parse/'
#     myobj = {
#         "text": text,
#         "message_id": "b2831e73-1407-4ba0-a861-0f30a42a2a5a"
#     }
#     x = requests.post(url, json=myobj)
#     y = json.loads(x.text)
#     return y["intent"]['name']



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
