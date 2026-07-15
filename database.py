import sqlite3

conn = sqlite3.connect("emocare.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emotion TEXT,
    confidence REAL,
    date TEXT,
    time TEXT
)
""")
# Check if admin already exists
cursor.execute("SELECT * FROM users WHERE email=?", ("admin@emocare.com",))

if cursor.fetchone() is None:
    cursor.execute(
        "INSERT INTO users(name,email,password) VALUES(?,?,?)",
        ("Administrator", "admin@emocare.com", "admin123")
    )

conn.commit()
conn.close()

print("Database Ready!")