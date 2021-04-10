# Shorten URL service

## Installation instructions

1. Clone the repo. Additional instructions (credentials) can be found [here](https://app.codesubmit.io/c/finn-gmbh/08f53aee-efa6-4ba5-8c74-b9260287d048/90496266-d2d5-4359-b357-c630c9c9240c).

```bash
$ git clone https://finn-gmbh-dreamy-banach@git.codesubmit.io/finn-gmbh/the-shortest-url-1-wcbrhr
$ cd the-shortest-url-1-wcbrhr
```


2. Setup a python virtual environment and install dependencies.

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install --upgrade pip wheel setuptools
$ pip install -r requirements.txt
$ python setup.py develop
```

3. Create the `instance/config.json` file. A sample with smart defaults is provided which can be copied from.

```bash
cp instance/config.json.sample instance/config.json
```

## Initialize the database

```bash
$ flask init-db
```

## Run the server locally

```bash
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run
```

## Launch SwaggerUI

Navigate to http://localhost:5000/apidocs.

## Build and view API docs

## Run tests
```bash
pytest
```
## Troubleshooting tips

## Known issues
- An `sqlite3.ProgrammingError` exception is thrown while exiting the server. 
```
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread.
```

## TODO

- installation instructions
- api tests with response code
- response structure
- error handling
- add requirements.txt