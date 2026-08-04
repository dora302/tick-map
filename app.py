from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# static 폴더를 프론트엔드가 접근할 수 있도록 연결
# (ticks_countries.geojson 파일이 static/ 폴더 안에 들어있어야 합니다!)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 1. 메인 접속 시 index.html 지도를 보여주는 루트 경로
@app.get("/", response_class=HTMLResponse)
def read_index():
    return FileResponse("index.html")

# 2. 서버가 잘 켜졌는지 확인하는 테스트 API
@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "진드기 역학 지도 서버 작동 중"}

if __name__ == "__main__":
    import uvicorn
    print("🚀 진드기 역학 지도 서버가 시작됩니다! http://127.0.0.1:8000 접속하세요.")
    uvicorn.run(app, host="127.0.0.1", port=8000)