# label-it

## How to install
Client
```
$ cd client
$ npm install
```
Server
```
$ cd server

On Linux:
$ python3 -m venv venv
On Windows:
$ py -3 -m venv venv

On Linux:
$ . venv/bin/activate
On Windows:
$ venv\Scripts\activate

$ pip install -r requirements.txt
$ set FLASK_APP=app.py
```
Database
```
python manage.py db upgrade
```

## How to run
Server
```
$ cd server
$ set FLASK_ENV=development 
$ flask run
```
Client
```
$ cd client
$ npm run serve
```

## Database migrations
```
$ python manage.py db migrate
$ python manage.py db upgrade
```
