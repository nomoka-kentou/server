from fastapi import FastAPI
import mysql.connector

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI with MySQL!"}