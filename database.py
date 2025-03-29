from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///points.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class PointHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)  # "YYYY-MM-DD" 形式
    site = db.Column(db.String(50), nullable=False)
    points = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<PointHistory {self.date} {self.site} {self.points}>'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    print("データベースを作成しました。")
