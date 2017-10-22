from flask import Flask, render_template
from morselate import morselate, MORSECODES

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', codes=MORSECODES)

@app.route("/encode/<text>")
def encode(text):
    text = text.replace("!","/").split(' ')
    return morselate.emorse(text)

@app.route("/decode/<morse>")
def decode(morse):
    return morselate.demorse(morse.split(' '))
