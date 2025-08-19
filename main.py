from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def index():
    return {"message":"Index page API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,port=8080)