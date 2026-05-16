from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pathlib import Path
import os

app = FastAPI(title="Minimal Blog")

# 获取当前文件所在目录
BASE_DIR = Path(__file__).parent


@app.get("/api/posts")
async def get_posts():
    return [
        {
            "id": 1,
            "title": "👋 Hello FastAPI",
            "date": "2024-05-01",
            "content": "这是我的第一篇博客。",
        },
        {
            "id": 2,
            "title": "📚 Python 学习笔记",
            "date": "2024-05-10",
            "content": "Python 语法简洁优雅。",
        },
        {
            "id": 3,
            "title": "⚡ 静态页面的动态感",
            "date": "2024-05-15",
            "content": "通过 Fetch API 请求后端 JSON。",
        },
    ]


@app.get("/")
async def root():
    html_path = BASE_DIR / "static" / "index.html"
    return FileResponse(html_path)


@app.get("/{path:path}")
async def static_files(path: str):
    file_path = BASE_DIR / "static" / path
    if file_path.exists() and file_path.is_file():
        return FileResponse(file_path)
    return JSONResponse({"detail": "Not Found"}, status_code=404)


# Vercel 需要的 handler
handler = app
