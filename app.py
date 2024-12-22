from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('crypto.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/cryptocurrencies', methods=['GET'])
def get_cryptocurrencies():
    conn = get_db_connection()
    cryptocurrencies = conn.execute('SELECT * FROM cryptocurrencies').fetchall()
    conn.close()
    return jsonify([dict(row) for row in cryptocurrencies])

@app.route('/cryptocurrencies', methods=['POST'])
def add_cryptocurrency():
    new_crypto = request.json
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO cryptocurrencies (name, price, futures, exchanges, staking_rate)
        VALUES (?, ?, ?, ?, ?)
    ''', (new_crypto['name'], new_crypto['price'], new_crypto['futures'], new_crypto['exchanges'], new_crypto['staking_rate']))
    conn.commit()
    conn.close()
    return '', 201

if __name__ == '__main__':
    app.run(debug=True)
