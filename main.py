from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from Books.routers import  router as books_router
from  sqlalchemy.schema import MetaData
from Database.database import base,engine

from Books import models

models.base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(books_router)

@app.get("/")
async def index():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",port=8080,reload=True)