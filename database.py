import sqlite3

DB_NAME = "codes.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CodeSnippets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL,
            language TEXT,
            output TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_code(code, language, output):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO CodeSnippets (code, language, output) VALUES (?, ?, ?)", (code, language, output))
    conn.commit()
    conn.close()

def fetch_code_history():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CodeSnippets ORDER BY timestamp DESC")
    data = cursor.fetchall()
    conn.close()
    return data

create_table()
