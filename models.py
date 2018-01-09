from app import db
from hashutils import make_pw_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    pw_hash = db.Column(db.String(120))
    movies = db.relationship('Movie', backref='owner')
    
    def __init__(self, email, password):
        self.email = email
        self.pw_hash = make_pw_hash(password)
    
    def __repr__(self):
        return '<User %r>' % self.email

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    watched = db.Column(db.Boolean)
    rating = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, owner):
        self.name = name
        self.watched = False
        self.owner = owner

    def __repr__(self):
        return '<Movie %r>' % self.name
