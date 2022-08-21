from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/user/{user_id}")
async def get_user_by_id(user_id: str):
    print("taheck")
    return {"message": f"Hello {user_id}"}


