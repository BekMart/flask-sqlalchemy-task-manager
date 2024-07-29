import os # to utilise enviroment variables within this file
from taskmanager import app # import app variable created within taskmanager packagem defined in the init file


if __name__ == "__main__": # tell the app how and where to run the application. name class must equal the default 'main' string
    app.run( # to get the app running we need 3 arguements..
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")), # needs to be an integer first
        debug=os.environ.get("DEBUG")
    ) # each of the arguements are stored in enviroment variables so need to use os.environ.get()

