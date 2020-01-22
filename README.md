# Bottle REST

Bottle backend with a client in python to read a csv file, submit to server, get results and save in a csv file.

### Installation

This code requires [Python](https://www.python.org) v3.6+ to run.

1. Clone repository
```sh
$ git clone https://github.com/kogakenji/bottleREST.git
```
2. Create and activate the Virtual environment
```sh
$cd bottleREST #enter the cloned repository
$ python3 -mvenv env #create virtual environment with name env
$ source env/bin/activate #activate virtual environment
(env) $ pip install -r requirements.txt # install requirements
```

### Executing server
```sh
(env) $ python bottlews.py
Bottle v0.12.14 server starting up (using WSGIRefServer())...
Listening on http://localhost:8080/
Hit Ctrl-C to quit.
```
### Executing test client (open in a separate terminal, remember to activate environment)
```sh
(env) $ python client_iselect.py
```

