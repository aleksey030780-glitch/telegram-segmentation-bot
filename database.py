import sqlite3

conn = sqlite3.connect("leads.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS leads (
    telegram_id INTEGER,
    username TEXT,
    source TEXT,
    industry TEXT,
    scale TEXT,
    pain TEXT,
    warmth TEXT,
    name TEXT,
    phone TEXT,
    created_at TEXT
)
""")

conn.commit()


def save_lead(data):
    cursor.execute("""
        INSERT INTO leads VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
    """, (
        data["telegram_id"],
        data["username"],
        data["source"],
        data["industry"],
        data["scale"],
        data["pain"],
        data["warmth"],
        data["name"],
        data["phone"]
    ))
    conn.commit()
