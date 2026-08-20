from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps Foundation Project is running!"

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/db-check")
def db_check():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DATABASE_HOST"),
            port=os.getenv("DATABASE_PORT"),
            database=os.getenv("DATABASE_NAME"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD")
        )
        conn.close()
        return {"database": "connected"}
    except Exception as e:
        return {"database": "error", "message": str(e)}, 500

@app.route("/redis-check")
def redis_check():
    try:
        r = redis.Redis(
            host=os.getenv("REDIS_HOST"),
            port=os.getenv("REDIS_PORT")
        )
        r.ping()
        return {"redis": "connected"}
    except Exception as e:
        return {"redis": "error", "message": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
