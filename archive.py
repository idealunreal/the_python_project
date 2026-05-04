import sqlite3
from datetime import datetime

DB_NAME = "archive.db"

def archive_operation(a: float, b: float, operation: str, result: float) -> None:
    """
    Archive the calculation operation and result to a local SQLite database.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            a REAL,
            b REAL,
            operation TEXT,
            result REAL,
            timestamp TEXT
        )
    ''')

    # Insert the record
    timestamp = datetime.now().isoformat()
    cursor.execute('''
        INSERT INTO calculations (a, b, operation, result, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (a, b, operation, result, timestamp))

    conn.commit()
    conn.close()