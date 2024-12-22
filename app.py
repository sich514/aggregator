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

if __name__ == '__main__':
    app.run(debug=True)
