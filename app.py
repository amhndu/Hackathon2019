from flask import Flask, request
app = Flask(__name__)

import redact

@app.route('/')
def home():
    return '''
<form method="post" action="/redact">
<textarea width="50%" name="text"></textarea>
<input type="submit"/>
</form>'''

@app.route('/redact', methods=['POST'])
def redact_view():
    try:
        text = request.form['text']
        return redact.redact(text)
    except KeyError:
        return 'No text'
