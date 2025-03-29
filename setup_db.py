"""
仮のpoints.dbを作成するためのスクリプト
"""

import sqlite3

# SQLite データベースに接続（なければ作成される）
conn = sqlite3.connect('instance/points.db')
cursor = conn.cursor()

# 既存のテーブルがあれば削除（テスト用のため）
cursor.execute("DROP TABLE IF EXISTS points")

# `points` テーブルを作成
cursor.execute("""
CREATE TABLE points (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    points INTEGER NOT NULL,
    site TEXT NOT NULL
)
""")

# 仮データを挿入
test_data = [
    ("2025-03-25", 25000, "SBI証券"),
    ("2025-03-26", 20000, "Amazon"),
    ("2025-03-27", 22000, "楽天証券"),
    ("2025-03-28", 25000, "SBI証券"),
    ("2025-03-29", 29000, "SBI証券"),
]

cursor.executemany("INSERT INTO points (date, points, site) VALUES (?, ?, ?)", test_data)

# 変更を保存して接続を閉じる
conn.commit()
conn.close()

print("仮の points.db を作成しました！")
