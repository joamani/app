from flask import Flask, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('ips.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ips (id INTEGER PRIMARY KEY, ip TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def get_ip():
    client_ip = request.remote_addr
    reversed_ip = '.'.join(client_ip.split('.')[::-1])
    save_ip(reversed_ip)
    return f'Reversed IP: {reversed_ip}', 200

def save_ip(ip):
    conn = sqlite3.connect('ips.db')
    c = conn.cursor()
    c.execute("INSERT INTO ips (ip) VALUES (?)", (ip,))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=80)
