- Setup a virtual environment (optional).
- `pip install -r requirements.txt`
- Rename `secret.py.sample` to `secret.py` and substitute api keys/secrets there
- Linux:
```
export FLASK_ENV=development
export FLASK_APP=app.py
```
Windows:
```
set FLASK_ENV=development
set FLASK_APP=app.py
```
Common:
```
flask run
```
