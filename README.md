## A basic Flask Application
This template Flask application uses 
  - Blueprints    : to modularize our app
  - SQLalchemy    : for object relational mapping. Manage the db with Python
  - Flask-Migrate : automate the db maintenance whenever the schema is changed
  - Flask-User    : a fantastic, fully functional login system which includes user roles

I'm keeping a copy here since it's the perfect starting point to actually start building an application. Others are welcome to use it.

#### Getting started
Make a new folder and clone the repository
```git
git clone git@github.com:rteuwens/basic_flask_app.git
cd basic_flask_app
```

#### Virtual Environment & Requirements
Create a virtual environment and activate it. 
I use virtualenv and write the following in a bash terminal:
```sh
     pip install virtualenv 
     virtualenv <nameofenv>
iOS: source <nameofenv>/bin/activate
Win: source <nameofenv>/Scripts/activate
```
Then cd to the directory where requirements.txt is located and run:
```sh
pip install -r requirements.txt
```

NOTE: you might run into an error when installing mysqlclient. It will complain about needing Visual Studio 14.0. <br>
This is an extremely annoying bug and I was not able to resolve it using the suggestions. <br>
Instead, just download the wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient and pip install it manually.
In my case, it was:
```sh
pip install <nameofenv>/mysqlclient-1.4.2-cp37-cp37m-win32.whl
```

#### Configuring the application 
It is currently set up to link to a MySQL database in the back-end, but you can configure this to any other relational database in config.py by changing the URI.
Whatever you choose, make sure the database exists. For MySQL, the command is simply:
```mysql
Enter password: <yourpassword>
CREATE DATABASE <yourdbname>;
USE <yourdbname>;
```
Make sure your env variables are set (reboot might be needed). If your auth for your localhost's mysql isn't simply root:admin, don't forget to change the URI.
```python
""" dev/localhost config """
    # fetching from user environment variables
    localhost_dbname = os.environ.get('MYSQL_LOCALHOST_DBNAME')

    # setting parameters
    SQLALCHEMY_DATABASE_URI = f'mysql://root:admin@localhost/{localhost_dbname}'
```
```python
""" production config """
    # fetching from user environment variables
    username = os.environ.get('MYSQL_USERNAME')
    password = os.environ.get('MYSQL_PASSWORD')
    hostname = os.environ.get('MYSQL_HOSTNAME')
    port = os.environ.get('MYSQL_PORT')
    dbname = os.environ.get('MYSQL_DBNAME')
    
    # setting parameters
    SQLALCHEMY_DATABASE_URI = f'mysql://{username}:{password}@{hostname}:{port}/{dbname}'
```

#### Setting up the database
Let's launch the app on our local device (localhost). In a bash terminal, write the following:
```sh
export FLASK_APP=run.py
export FLASK_ENV=development
```
Then set up the database migration schemes. A folder called "migrations/" will pop up.
```
flask db init
flask db migrate
flask db upgrade
```

#### Launching the app
```sh
flask run
```

# Happy building!
I was stuck in tutorial purgatory for a while, so hopefully this provides you with the foundation to quickly get 
to work with your web application using Flask, without having to worry about integrating login systems, etc.
Leverage the modularity of the Blueprints and make your own routes. 

To further customize Flask-User's templates, consult: https://flask-user.readthedocs.io/en/latest/customizing_forms.html
I've left an example of how I edited the main login page, that should give you a clue as to how to proceed.

