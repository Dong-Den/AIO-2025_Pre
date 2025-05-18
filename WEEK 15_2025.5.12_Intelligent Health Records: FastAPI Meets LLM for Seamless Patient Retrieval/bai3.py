# API thông tin người dùng
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: EmailStr

@app.post("/user")
async def create_user(user: User):
    return {
        "name": user.name,
        "age": user.age,
        "email": user.email,
        "is_adult": user.age >=18
    }


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
