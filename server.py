from flask import Flask, request
import socket
app = Flask(__name__)
seed = 0

@app.route('/', methods=['POST','GET'])
def process_json():
    global seed
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.get_json()
            seed = json['num']
            subprocess.Popen(["/home/ubuntu/python3","/home/ubuntu/stress_cpu.py"])
        return 'Updated seed to ' + str(seed)
    elif request.method == 'GET':
        return socket.gethostbyname(socket.gethostname())
    else:
        return 'Error in request'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, debug=True)