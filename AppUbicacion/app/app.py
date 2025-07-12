from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "db"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "password"),
        database=os.environ.get("DB_NAME", "ecuador")
    )

server_name = os.environ.get("SERVER_NAME", "Servidor")

@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM provincias')
    provincias = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', provincias=provincias, server_name=server_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
