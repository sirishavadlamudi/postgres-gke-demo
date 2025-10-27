from flask import Flask
import os
import psycopg2

app = Flask(__name__)

DB_HOST = os.environ.get("POSTGRES_HOST", "postgres")
DB_NAME = os.environ.get("POSTGRES_DB", "pgdb")
DB_USER = os.environ.get("POSTGRES_USER", "pguser")
DB_PASS = os.environ.get("POSTGRES_PASSWORD", "pgpassword")

@app.route("/")
def index():
    try:
        conn = psycopg2.connect(
            host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS, connect_timeout=3
        )
        conn.close()
        return "OK, DB reachable", 200
    except Exception as e:
        return f"DB not reachable: {e}", 500
