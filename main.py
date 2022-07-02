from fastapi import Depends, FastAPI
from database import engine
import users.models, properties.models, attorneys.models, agents.models, contracts.models, clients.models
import users.main, properties.main, attorneys.main, agents.main, contracts.main, clients.main


users.models.Base.metadata.create_all(bind=engine)
properties.models.Base.metadata.create_all(bind=engine)
attorneys.models.Base.metadata.create_all(bind=engine)
agents.models.Base.metadata.create_all(bind=engine)
contracts.models.Base.metadata.create_all(bind=engine)
clients.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.main.router)
app.include_router(properties.main.router)
app.include_router(attorneys.main.router)
app.include_router(agents.main.router)
app.include_router(contracts.main.router)
app.include_router(clients.main.router)
