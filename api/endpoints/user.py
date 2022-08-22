from fastapi import APIRouter, Depends, HTTPException, Query

router = APIRouter()


@router.get("/{user_id}")
async def get_user_by_id(user_id: str):
    print("Get User by Id")
    return {"message": f"Hello {user_id}"}


@router.post("/")
async def save_user():
    print("Create User")
    return {"message": f"Hello "}


@router.post("/{user_id}", status_code=200)
async def save_user(user_id: str):
    print("Update User")
    return {"message": f"Hello {user_id}"}
