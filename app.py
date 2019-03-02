from flask import Flask, request, render_template
app = Flask(__name__)

import redact

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/redact', methods=['POST'])
def redact_view():
    error = ''
    try:
        text = request.form['text']
        redacted_results = redact.redact(text)
        print('redacted:', redacted_results)
        return render_template("redact.html", redacted_results=redacted_results)
    except KeyError:
        error = 'No text'
        return render_template("redact.html", error=error)
