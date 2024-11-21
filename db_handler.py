import sqlite3
import pandas as pd

DB_FILE = "mutual_funds.db"

def save_to_db(data: pd.DataFrame):
    try:
        conn = sqlite3.connect(DB_FILE)
        data.to_sql("mutual_funds", conn, if_exists="append", index=False)
        conn.close()
        print("Data saved successfully.")
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
