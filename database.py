from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PointHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    site = db.Column(db.String(100), nullable=False)
    points = db.Column(db.Integer, nullable=False)

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///points.db'  # SQLiteを使用
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
