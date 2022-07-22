from fastapi import Depends, FastAPI
from database import engine
from fastapi.middleware.cors import CORSMiddleware
import users.models, properties.models, attorneys.models, agents.models, contracts.models, clients.models, albums.models
import users.main, properties.main, attorneys.main, agents.main, contracts.main, clients.main, albums.main
import uvicorn

users.models.Base.metadata.create_all(bind=engine)
properties.models.Base.metadata.create_all(bind=engine)
attorneys.models.Base.metadata.create_all(bind=engine)
agents.models.Base.metadata.create_all(bind=engine)
contracts.models.Base.metadata.create_all(bind=engine)
clients.models.Base.metadata.create_all(bind=engine)
albums.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.main.router)
app.include_router(properties.main.router)
app.include_router(attorneys.main.router)
app.include_router(agents.main.router)
app.include_router(contracts.main.router)
app.include_router(clients.main.router)
app.include_router(albums.main.router)


'''Cross Origin Resource Sharing'''
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)