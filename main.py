from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from sqlalchemy.schema import MetaData
from database.database import base,engine
from starlette.middleware.cors import CORSMiddleware

from books.routers import  router as books_router
from auth.router import auth_router
from user.router import user_router

base.metadata.create_all(bind=engine)
openapi_tags = [
    {
        "name": "Users",
        "description": "User operations",
    },
    {
        "name": "Books",
        "description":"Book operations",
    }
]

app = FastAPI(openapi_tags=openapi_tags)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router, prefix='/api')
app.include_router(user_router, prefix='/api', tags=['Users'])
app.include_router(books_router)

@app.get("/")
async def index():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",port=8080,reload=True)