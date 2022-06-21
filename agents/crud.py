from sqlalchemy.orm import Session
from . import models, schemas


def create_agent(db: Session, agent: schemas.Agent):
    agent = models.Agent(name=agent.name, phone=agent.phone, organization=agent.organization)
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent

def get_agent_by_name(db: Session, name: str):
    return db.query(models.Agent).filter(models.Agent.name == name).first()

def get_agents(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Agent).offset(skip).limit(limit).all()

def delete_agent(db: Session, agent_id: int):
    agent = db.query(models.Agent).filter(models.Agent.id == agent_id).first()
    db.delete(agent)
    db.commit()
    return agent
