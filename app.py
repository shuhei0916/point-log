from flask import Flask, jsonify
import csv

app = Flask(__name__)

# CSVからポイントデータを読み込むエンドポイント
@app.route('/get_points', methods=['GET'])
def get_points():
    points = []
    with open('points.csv', mode='r') as file:
        reader = csv.reader(file)
        # CSVからデータをリストに変換
        for row in reader:
            points.append({'date': row[0], 'points': row[1], 'site': row[2]})
    return jsonify(points)

if __name__ == "__main__":
    app.run(debug=True)
