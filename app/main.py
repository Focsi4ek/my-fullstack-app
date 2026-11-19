from fastapi import FastAPI

app = FastAPI(title="My Fullstack App")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI with Postgres!"}