from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit

app = Flask(__name__)
app.debug=True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

switchstate = False


@app.route("/")
def hello():
    return render_template('test.html')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('my event')
def handle_my_custom_event(json):
	print str(json)
	emit('message', json)

@socketio.on('getStatus')
def sendstate():
	# print str(json)
	emit('Status', switchstate)

@socketio.on('updateStatus')
def sendstate(state):
	# print str(json)
	switchstate = state
	emit('Status', switchstate,broadcast=True)

if __name__ == '__main__':
    socketio.run(app)