from uuid import UUID
from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role, UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("c6e4471a-be8c-4c77-bdc9-f891516c35aa"),
        first_name="Sehmus",
        last_name="Acar",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("7b769d34-e3fc-4226-87d8-388883421d96"),
        first_name="Furki",
        last_name="Ornek",
        gender=Gender.male,
        roles=[Role.admin,Role.user]
    )
]


@app.get("/")
async def root():
    return {"message": "Hello "}


@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async  def register_user(user:User):
    db.append(user)
    return {'id':user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code= 404,
        detail=f'user with id: {user_id} does not exists'
    )

@app.put("api/v1/users/{user_id}")
async def update_user(user_update:UserUpdateRequest,user_id:UUID):
    for user in db:
        if user_update.first_name is not None:
            user.first_name = user_update.first_name
        if user_update.last_name is not None:
            user.last_name = user_update.last_name
        if user_update.middle_name is not None:
            user.middle_name = user_update.middle_name
        if user_update.roles is not None:
            user.roles = user_update.roles
        return
    raise HTTPException(
        status_code=404,
        detail=f'user with id: {user_id} does not exists'
    )