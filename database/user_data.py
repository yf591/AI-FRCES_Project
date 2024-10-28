import sqlite3
import datetime

DATABASE_FILE = 'user_data.db'  # データベースファイル名

def create_table():
    """ユーザーデータテーブルを作成する"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS food_waste_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            food_type TEXT,
            weight REAL,
            cost REAL,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()


def insert_data(user_id, food_type, weight, cost):
    """食品廃棄データをデータベースに挿入する"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    timestamp = datetime.datetime.now().isoformat()
    cursor.execute('''
        INSERT INTO food_waste_data (user_id, food_type, weight, cost, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, food_type, weight, cost, timestamp))

    conn.commit()
    conn.close()

def get_data(user_id):
  """ユーザーの食品ロスデータを取得する"""
  conn = sqlite3.connect(DATABASE_FILE)
  cursor = conn.cursor()

  cursor.execute("SELECT * FROM food_waste_data WHERE user_id=?", (user_id,))
  data = cursor.fetchall()
  conn.close()
  return data


# テーブルを作成 (一度だけ実行すればOK)
create_table()