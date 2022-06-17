import crud, models, schemas
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from werkzeug.security import check_password_hash

app = FastAPI()

users.models.Base.metadata.create_all(bind=engine)
properties.models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(users.main.router)
app.include_router(posts.main.router)
