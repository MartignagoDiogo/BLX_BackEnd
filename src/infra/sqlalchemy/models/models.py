from typing import Optional
from pydantic.main import BaseModel
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.sql.sqltypes import Boolean
from src.infra.sqlalchemy.config.database import Base


class Produto(Base):
    
    __tablename__ = 'produto'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    detalhe = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    tamanho = Column(String)
    
class Usuario(Base):
    
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
     
    

    
    