from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="demo-backend")


# 请求体格式定义：前端 POST /api/greet 时按这个结构传 JSON
# name 和 times 都有默认值，所以传空 {} 也合法
class GreetRequest(BaseModel):
    name: str = "world"
    times: int = 1


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/api/message")
def message():
    return {"message": "Hello from backend service"}


# 交互式接口：接收 {"name", "times"}，返回打招呼消息
# "from": "backend" 是给前端的标记，前端页面据此显示消息来源
@app.post("/api/greet")
def greet(req: GreetRequest):
    msg = " ".join([f"Hello, {req.name}!"] * max(1, req.times))
    return {"message": msg, "from": "backend"}
