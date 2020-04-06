from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "pravanya"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:gopireddy@localhost/"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Result(db.Model):
    __tablename__ = "git_sample"
    id = db.Column(db.Integer, primary_key=True)
    fname=db.column(db.String(20))
    lname=db.column(db.String(20))
    gender=db.column(db.String(5))
    email = db.Column(db.String(50), unique=True)


    def __init__(self,id,fname,lname,gender,email):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.gender=gender
        self.email = email

@app.route('/')
def index():
    return "hello"
@app.route('/<name>/<email>/<gender>')
def index1():
    return f"fnmae:{name},email:{email},gender:{gender}"
@app.route('/<name>')
def index2(name):
    return fname
