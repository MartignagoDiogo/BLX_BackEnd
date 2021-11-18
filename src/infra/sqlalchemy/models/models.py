from typing import Optional
from pydantic.main import BaseModel
from sqlalchemy import Column, String, Float
from sqlalchemy.sql.sqltypes import Boolean
from infra.sqlalchemy.config.database import Base


class Produto(Base):
    
    __tablename__ = 'produto'
    
    id = Column(String, primary_key=True, index=True)
    nome = Column(String)
    detalhe = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    
class Usuario(Base):
    
    __tablename__ = 'usuario'
    
    id = Column(String, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
     
    

    
    