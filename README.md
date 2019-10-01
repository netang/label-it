# label-it

## How install
```
$ cd client
$ npm install
```
```
$ cd server
$ python -3 -m venv venv
$ venv/Scripts/activate
$ pip install Flask psycopg2 Flask-SQLAlchemy Flask-Migrate Flask-Script Flask-Cors
$ set FLASK_APP=app.py
```

## How run
Server run
```
$ cd server
$ set FLASK_ENV=development 
$ flask run
```
Client run
```
$ cd client
$ npm run serve
```

## Database migrations
```
$ python manage.py db migrate
$ python manage.py db upgrade
```
