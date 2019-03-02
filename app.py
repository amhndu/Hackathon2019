from flask import Flask, request, render_template
app = Flask(__name__)

import redact

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/redact', methods=['POST'])
def redact_view():
    try:
        text = request.form['text']
        return redact.redact(text)
    except KeyError:
        return 'No text'
