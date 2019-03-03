## Running with docker
- Clone the repo
- Copy `secret.py.sample` to `secret.py` and substitute api keys/secrets there
- Run `docker build --tag=hackathon2019 .` to build the docker image
- Then `docker run -p 5000:80 hackathon2019` to launch it at port `5000`

## Running Locally
- Setup a virtual environment (optional).
- `pip install -r requirements.txt`
- Copy `secret.py.sample` to `secret.py` and substitute api keys/secrets there
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
