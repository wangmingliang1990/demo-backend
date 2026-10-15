from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="demo-backend")


class GreetRequest(BaseModel):
    name: str = "world"
    times: int = 1


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/api/message")
def message():
    return {"message": "Hello from backend service"}


@app.post("/api/greet")
def greet(req: GreetRequest):
    msg = " ".join([f"Hello, {req.name}!"] * max(1, req.times))
    return {"message": msg, "from": "backend"}
