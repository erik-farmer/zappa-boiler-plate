from db import db

class Foo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
