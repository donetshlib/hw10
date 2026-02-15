import os
import psycopg2
from fastapi import FastAPI

app = FastAPI()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://app_user:app_pass@db:5432/app_db"
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    value = cur.fetchone()[0]
    cur.close()
    conn.close()
    return {"db": "connected", "select_1": value}
