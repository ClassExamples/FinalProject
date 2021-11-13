from flask import Flask
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:1qaz2wsx@aa1kazwout7c7ew.cijoy5ie4vma.us-east-2.rds.amazonaws.com/ebdb'
db = SQLAlchemy(application)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

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

if __name__=="__main__":
    application.run(debug=True)