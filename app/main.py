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
    # 【毕业演示】在消息尾部追加签名：
    #   - 只在末尾加后缀，"Hello, xxx!" 主体原样保留，
    #     所以前端 e2e（断言包含 "Hello, ci!"）和产品冒烟（断言包含 "Hello, Product"）都不受影响
    #   - 这就是"契约兼容的增量变更"：改实现、不破接口，下游测试自然全绿
    msg += " [auto-deployed by CI]"
    return {"message": msg, "from": "backend"}
