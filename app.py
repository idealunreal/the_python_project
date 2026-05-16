from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
from pathlib import Path

app = FastAPI(title="Minimal Blog")


# 先定义 API 路由（必须在 mount 之前）
@app.get("/api/posts")
async def get_posts():
    return [
        {
            "id": 1,
            "title": "👋 Hello FastAPI",
            "date": "2024-05-01",
            "content": "这是我的第一篇博客，使用 FastAPI + 原生 JS 构建。",
        },
        {
            "id": 2,
            "title": "📚 Python 学习笔记",
            "date": "2024-05-10",
            "content": "Python 语法简洁优雅，配合异步编程非常适合现代 Web 开发。",
        },
        {
            "id": 3,
            "title": "⚡ 静态页面的动态感",
            "date": "2024-05-15",
            "content": "通过 Fetch API 请求后端 JSON，无需刷新页面即可渲染内容。",
        },
    ]


# 根路径返回 index.html
@app.get("/")
async def root():
    return FileResponse("static/index.html")


# 最后挂载静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
