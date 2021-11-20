from typing import Optional
from pydantic.main import BaseModel
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean
from src.infra.sqlalchemy.config.database import Base


class Usuario(Base):
    
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
    senha = Column(String)
    
    produtos = relationship('Produto', back_populates='usuario')



class Produto(Base):
    
    __tablename__ = 'produto'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    detalhe = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    tamanho = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuario.id', name='fk_usuario'))
    
    usuario = relationship('Usuario', back_populates='produtos')

     
    

    
    