from fastapi import FastAPI
from fastapi.responses import RedirectResponse


app = FastAPI()

@app.get("/")
async def index():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",port=8080,reload=True)