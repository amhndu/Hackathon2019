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
        redacted_text = redact.redact(text)
    except KeyError:
        redacted_text = 'No text'
    return render_template("redact.html", text=redacted_text)
