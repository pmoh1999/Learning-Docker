# app.py

import os

from flask import Flask
import MySQLdb

app = Flask(__name__)

DB_HOST = os.getenv("MYSQL_HOST", "db")
DB_USER = os.getenv("MYSQL_USER", "root")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD", "my-secret-pw")
DB_NAME = os.getenv("MYSQL_DB", "mysql")


@app.route('/')
def hello_world():
    try:
        db = MySQLdb.connect(
            host=DB_HOST,
            user=DB_USER,
            passwd=DB_PASSWORD,
            db=DB_NAME,
        )
        cur = db.cursor()
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()
        db.close()

        if version is None:
            return 'Hello, World! MySQL is reachable but returned no version.'

        return f'Hello, World! MySQL version: {version[0]}'
    except Exception as exc:
        return f'Hello, World! MySQL connection failed: {exc}', 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)