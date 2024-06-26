import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True": # new if line for deployment

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

else: # new else staement for deployment
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
         uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)

from taskmanager import routes  # no quality assurance