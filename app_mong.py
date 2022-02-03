from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_migrate import Migrate
from flask_pymongo import PyMongo
from flask_login import  (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required
)

mongo = PyMongo()
bcrypt = Bcrypt()


login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"

def create_app():
    app = Flask(__name__)

    app.secret_key = 'secret-key'
    app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db" # makes it a file called databse.db
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    login_manager.init_app(app)
    # db.init_app(app)
    # migrate.init_app(app, db)
    # bcrypt.init_app(app)
    return app

app = create_app()
# mocking up login with flask_login


#TODO: mockup sqlalchemy
#TODO: mockup mongodb


@app.route('/')
def hello_world():  # put application's code here
    write_user_sqlalchemy("helloemail","password")
    return 'Hello World!'

def write_user_mongo():
    pass
class MUser():
    def __init__(self, username, password):
        self.username = username
        self.password = password

def write_user_sqlalchemy(username, password) -> bool:
    """
    :param username:
    :param password:
    :return: bool logged in properly
    """
    if SUser.query.filter_by(username = username, password=bcrypt.generate_password_hash(password)).first() is not None:
        print("error alrerady used")
        return False
    else:
        print("adding")
        newuser = SUser(username=username,password=bcrypt.generate_password_hash(password))
        db.session.add(newuser)
        db.session.commit()
    pass

class SUser(UserMixin, db.Model):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': 'true'}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False, unique=True)

    def __repr__(self):
        return '<User %r>' % self.username

if __name__ == '__main__':
    app.run()
