- Setup a virtual environment (optional).
- `pip install -r requirements.txt`
- Rename `secret.py.sample` to `secret.py` and substitute api keys/secrets there
- `FLASK_ENV=development FLASK_APP=app.py flask run`  
Note that `FLASK_ENV` sets debugging. You might need to use a different way to set `FLASK_APP` environment variable to `app.py` for windows and then run `app.py`

