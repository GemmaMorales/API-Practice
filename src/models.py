from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(80), unique=True, nullable=False)
    done = db.Column(db.Boolean(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Todos %r>' % self.label

    def serialize(self):
        return {
            "label": self.label,
            "done": self.done,
            "id": self.id
        }