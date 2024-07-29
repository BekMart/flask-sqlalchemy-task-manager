import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"): # if you can find a file path to an existing file called env.py..
    import env # import env. (because env.py is hidden we need to import it to use our hidden variables)

# create instance of the imported Flask() class stored in a variabled called 'app'
app = Flask(__name__) # __name__ is the defualt Flask module
# set up app configuration variables that will come from our enviroment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app) # create instance of imported SQLAlchemy() class to variable 'db' and set to the imstance of our Flask 'app'

from taskmanager import routes # needs to be imported after app and db are routes is reliant on them 