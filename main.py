import crud, models, schemas
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from werkzeug.security import check_password_hash
from jose import JWTError, jwt
from pydantic import BaseModel
import uvicorn

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

models.Base.metadata.create_all(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

class TokenData(BaseModel):
    email: str | None = None

class Token(BaseModel):
    access_token: str
    token_type: str

origins = ["*"]
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_username(get_db(), username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

def authenticate_user(username: str, password: str, db: Session):
    user = crud.get_user_by_username(db, username)
    if not user:
        return False
    if not check_password_hash(user.password, password):
        return False
    return user

async def get_current_active_user(current_user: models.User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

    
@app.get("/users/me")
async def read_users_me(current_user: models.User = Depends(get_current_active_user)):
    return current_user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/properties/", response_model=schemas.Property)
def create_property(property: schemas.Property, db: Session = Depends(get_db)):
    property_exists = crud.get_property_by_address(db, address=property.address)
    if property_exists:
        raise HTTPException(status_code=400, detail="Property already registered")
    return crud.create_property(db=db, property=property)

@app.get("/properties/", response_model=list[schemas.Property])
def read_properties(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    properties = crud.get_properties(db, skip=skip, limit=limit)
    return properties

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
