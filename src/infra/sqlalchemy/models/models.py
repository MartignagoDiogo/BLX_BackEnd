from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.sql.sqltypes import Boolean
from src.infra.sqlalchemy.config.database import Base


class Produto(Base):
    
    __tablename__ = 'produto'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    detalhe = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    
    