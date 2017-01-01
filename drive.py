import ginger
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

g = ginger.Ginger()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('forward')
def forward(message):
    g.forward()
    emit('msg', {'data': 'go'})

@socketio.on('reverse')
def forward(message):
    g.reverse()
    emit('msg', {'data': 'go'})

@socketio.on('left')
def forward(message):
    g.left()
    emit('msg', {'data': 'go'})

@socketio.on('right')
def forward(message):
    g.right()
    emit('msg', {'data': 'go'})

@socketio.on('disconnect')
def stop():
    g.stop()
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)
