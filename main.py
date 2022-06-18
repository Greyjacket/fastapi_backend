from fastapi import Depends, FastAPI
from database import engine
import users.models, properties.models
import users.main, properties.main


users.models.Base.metadata.create_all(bind=engine)
properties.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.main.router)
app.include_router(properties.main.router)
