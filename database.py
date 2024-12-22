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
    
    # Вставка данных
    cryptocurrencies = [
        ('Bitcoin (BTC)', 27000, 'Да', 'Binance, Coinbase', 6.5),
        ('Ethereum (ETH)', 1800, 'Да', 'Binance, Coinbase', 7.2),
        # Добавьте другие криптовалюты здесь
        ('Solana (SOL)', 214.444, 'Да', 'Binance, Coinbase', 0.43),
        ('XRP', 2.3597, 'Нет', 'Binance, Coinbase', 0.96)
    ]
    c.executemany('''
        INSERT INTO cryptocurrencies (name, price, futures, exchanges, staking_rate)
        VALUES (?, ?, ?, ?, ?)
    ''', cryptocurrencies)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
