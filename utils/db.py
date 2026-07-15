import sqlite3
from datetime import datetime

DB_NAME = "emocare.db"

def save_detection(emotion, confidence):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    now = datetime.now()

    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")

    cursor.execute(
        """
        INSERT INTO history(emotion, confidence, date, time)
        VALUES(?,?,?,?)
        """,
        (emotion, confidence, date, time)
    )

    conn.commit()
    conn.close()