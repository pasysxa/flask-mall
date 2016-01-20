from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
bcrypt = Bcrypt(app)


if __name__ == '__main__':
    print(app.config['DEBUG'])
    print(app.config['DATABASE_URI'])
    print(app.config['SECRET_KEY'])

