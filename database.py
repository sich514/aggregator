import sqlite3

def init_db():
    conn = sqlite3.connect('crypto.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS cryptocurrencies (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            futures TEXT NOT NULL,
            exchanges TEXT NOT NULL,
            staking_rate REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
