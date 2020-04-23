from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    auth_token = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, auth_token, email):
        self.auth_token = auth_token
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.id
