#Flask Template - multiple modules

Flask template using for large applications, as structure [recommended](http://flask.pocoo.org/docs/0.10/patterns/packages/)

Single module can be found [here](https://github.com/ctnx/python-flask-single)

## Structure
.
├── .gitignore
├── Procfile
├── README.md
├── hello.py
├── helloflask
│   ├── __init__.py
│   ├── auth.py
│   ├── models.py
│   ├── static
│   ├── templates
│   ├── views.py
├── requirements.txt
├── test.db

## Usage
Cloning using git:

``` git clone https://github.com/ctnx/python-flask-multiple helloflask ```

``` cd helloflask ```

``` git remote remove origin ```

## Requirements:
Requirements can be install via ```pip```

``` pip install -r requirements.txt ```

## Heroku Upload
The file Procfile is created only for use with Heroku. Feel free to delete it if you intend to use different service provider/ or run locally.
