from flask import Flask, render_template, jsonify
from database import db, PointHistory, init_db  # init_db をインポート

app = Flask(__name__)
init_db(app)  # データベースをアプリに登録

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_points', methods=['GET'])
def get_points():
    with app.app_context():
        data = PointHistory.query.all()
        results = [
            {"date": entry.date, "site": entry.site, "points": entry.points}
            for entry in data
        ]
    return jsonify(results)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # データベースとテーブルを作成
    app.run(debug=True)
    