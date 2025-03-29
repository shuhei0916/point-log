from flask import Flask, render_template, jsonify
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # index.htmlを表示

@app.route('/get_points', methods=['GET'])
def get_points():
    points = []
    with open('points.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            points.append({'date': row[0], 'points': row[1], 'site': row[2]})
    return jsonify(points)

if __name__ == "__main__":
    app.run(debug=True)
