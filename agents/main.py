from . import crud, schemas
from fastapi import Depends, APIRouter, HTTPException
from dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/agents",
)

@router.post("/", response_model=schemas.Agent)
def create_agent(agent: schemas.Agent, db: Session = Depends(get_db)):
    agent_exists = crud.get_agent_by_name(db, name=agent.name)
    if agent_exists:
        raise HTTPException(status_code=400, detail="Agent already registered")
    return crud.create_agent(db=db, agent=agent)


@router.get("/", response_model=list[schemas.Agent])
def read_agents(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    agents = crud.get_agents(db, skip=skip, limit=limit)
    return agents


@router.get("/{agent_name}", response_model=schemas.Agent)
def read_agent(name: str, db: Session = Depends(get_db)):
    agent = crud.get_agent_by_name(db, name=name)
    if agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent


@router.delete("/{agent_id}", response_model=schemas.Agent)
def delete_agent(agent_id: int, db: Session = Depends(get_db)):
    agent = crud.delete_agent(db, agent_id=agent_id)
    if agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent
