from flask import Flask,request
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
application = Flask(__name__)

DB_URI = os.environ.get("DB_URI")
DB_URI = "mysql+pymysql://admin:1qaz2wsx@aa1zsbav5cuxux.cijoy5ie4vma.us-east-2.rds.amazonaws.com:3306/ebdb"
application.config['SQLALCHEMY_DATABASE_URI'] = DB_URI #'mysql+pymysql://admin:1qaz2wsx@aa1zsbav5cuxux.cijoy5ie4vma.us-east-2.rds.amazonaws.com:3306/ebdb'
db = SQLAlchemy(application)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class UserProfilePic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    profile_pic = db.Column(db.String(500), unique=True, nullable=False)

    def __repr__(self):
        return '<User Profile Pic %r %s>' % self.username, self.profile_pic



db.create_all()


@application.route("/user/add")
def user_add():
    admin = User(username='admin', email='admin@example.com')
    db.session.add(admin)
    db.session.commit()
    return "Item add"

@application.route("/user/list")
def get_all_users():
    all = User.query.all()
    return f"{[u.email for u in all]}"

@application.route("/")
def index():
    return render_template("index.html")


@application.route("/item")
def item_add():
    return "Item add"


@application.route("/upload_image",methods=["GET","POST"])
def upload_image():
    print(request.method)
    if request.method =='POST':
        file = request.files['profile_pic']
        file_name = secure_filename(file.filename)
        print(file_name)
        file.save(file_name)
    return render_template("upload_image_form.html")


if __name__=="__main__":
    application.run(debug=True)