from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def exe_cursor_to_dict(cursor, sql):
    cursor.execute(sql)
    data = cursor.fetchall()
    results = []
    columns = [column[0] for column in cursor.description]
    for row in data:
        results.append(dict(zip(columns, row)))
    return results

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(post.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Vannq test fastapi python!"}

