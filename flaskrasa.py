import json
import requests
from flask import Flask,request
import os
app = Flask(__name__)

######POST request
@app.route('/upload_file', methods=["POST"])
def index():
    # read the nlu file
    # nlu_file = request.files['file']
    # nlu_file_str = nlu_file.read()
    # nlu_file_str_text_obj = nlu_file_str.decode('UTF-8')
    # #save to file
    # with open("data.txt", 'w+') as f:
    #     f.write(nlu_file_str_text_obj)
    # Since the project has the config file we can train rasa from a command
    cmd = 'rasa train nlu'
    os.system(cmd)  
    # url = 'http://localhost:5005/model/train'
    # payload = {
    #     "text": msg
    # }
    # x = requests.post(url, json=payload)
    # y = json.loads(x.text)
    # print(x.text)
    return "Done"
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)