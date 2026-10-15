# 后端服务的容器镜像定义
# 作用：把 "FastAPI 应用 + Python 运行环境" 打包成一个可以在任何机器上运行的镜像

# 基础镜像：精简版 Python 3.11（相当于一个只有 Python 的空系统）
FROM python:3.11-slim

# 容器内的工作目录，后续命令都在 /app 下执行
WORKDIR /app

# 先只拷贝依赖清单再安装 —— 这样只要 requirements.txt 没变，
# 改代码重新构建时就能复用缓存的依赖层，构建速度快很多
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 再把应用代码拷进镜像
COPY app ./app

# 声明服务监听端口（文档性质，真正生效靠下面的启动命令）
EXPOSE 8010

# 容器启动时执行的命令：用 uvicorn 跑 FastAPI 应用
# --host 0.0.0.0 让容器外的机器也能访问（写 127.0.0.1 就只有容器内部能访问）
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8010"]
