from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

#db.create_all()#create the initial database
admin = User(username='admin1', email='admin@example1.com')
guest = User(username='guest1', email='guest@example1.com')

#db.session.add(admin)#add to database
#db.session.add(guest)
#db.session.commit()

User.query.all()
s=User.query.all()
print(s)