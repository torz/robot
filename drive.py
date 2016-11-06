import ginger
from flask import Flask

g = ginger.Ginger()

app = Flask(__name__)

@app.route("/forward")
def forward():
    g.forward()
    return "forward"

@app.route("/reverse")
def reverse():
    g.reverse()
    return "/reverse"

@app.route("/left")
def left():
    g.left()
    return "left"

@app.route("/right")
def right():
    g.right()
    return "right"

@app.route("/")
def stop():
    g.stop()
    return "stop"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
