from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

class User(BaseModel):
    name: str
    password: str

engine = create_engine('sqlite:///./sql_app.db', echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class UserService:
    def __init__(self, session: SessionLocal):
        self.session = session

    def login(self, username: str, password: str) -> User:
        user = self.session.query(User).filter(User.name == username, User.password == password).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def register(self, username: str, password: str) -> User:
        user = User(name=username, password=password)
        self.session.add(user)
        self.session.commit()
        return user

app = FastAPI()

class LoginResponse(BaseModel):
    user: User

class RegisterResponse(BaseModel):
    user: User

@app.post("/login")
def login(username: str, password: str, user_service: UserService = Depends()) -> User: 
    return user_service.login(username, password)

@app.post("/register")
def register(username: str, password: str, user_service: UserService = Depends()) -> User:
    return user_service.register(username, password)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
