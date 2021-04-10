# Shorten URL service

## Installation instructions

1. Clone the repo

```bash
$ git clone https://finn-gmbh-dreamy-banach@git.codesubmit.io/finn-gmbh/the-shortest-url-1-wcbrhr
$ cd the-shortest-url-1-wcbrhr
```

2. Setup a python virtual environment and install dependencies

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install --upgrade pip wheel setuptools
$ pip install -r requirements.txt
$ python setup.py develop
```

3. Create the config.yml file. A sample with smart defaults is provided which can be copied from. Any changes required to the config will have to be made in the `config.yml` file. Note that if the filename of the sqlite database is changed, the same will need to be used in the following step.

```bash
cp config.yml.sample config.yml
```

## Setting up the database

```bash
$ sqlite3 /tmp/shortest_url.db
```

```bash
sqlite> CREATE TABLE IF NOT EXISTS urls_map (
	id INTEGER PRIMARY KEY,
   	short_url TEXT DEFAULT NULL,
	full_url TEXT DEFAULT NULL,
    created_at DATETIME DEFAULT (datetime('now', 'utc'))
);
```
## Run the server locally

```bash
$ export FLASK_APP=app.py
$ flask run
```
## Build and view API docs

## Run tests

## Troubleshooting tips

## Known issues

## TODO

- installation instructions
- api tests
- response structure
- error handling