from typing import Optional
from pydantic.main import BaseModel
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import column
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
    pedidos = relationship('Pedido', back_populates='usuario')


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
    
class Pedido(Base):
    __tablename__ = 'pedido'
    
    id = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer)
    local_entrega = Column(String)
    tipo_entrega = Column(String)
    observacao = Column(String)
    
    usuario_id = Column(Integer, ForeignKey('usuario.id', name='fk_usuario'))
    produto_id = Column(Integer, ForeignKey('produto.id', name='fk_pedido_produto'))
    
    usuario = relationship('Usuario', back_populates='pedidos')
    usuario = relationship('Usuario')
    
