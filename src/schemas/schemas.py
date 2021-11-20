from pydantic import BaseModel
from typing import List, Optional

from src.infra.sqlalchemy.models.models import Produto

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str 
    senha: str
    #produtos: Optional[Produto]
    
    class Config:
        orm_mode = True
    
class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhe: str
    preco: float
    disponivel: bool = False
    tamanho: str
    usuario_id: int
    usuario: Optional[Usuario]
    
        
    class Config:
        orm_mode = True
        
class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float
    usuario_id: int
    usuario: Optional[Usuario]

        
    class Config:
        orm_mode = True
            
    
#class Pedido(BaseModel):
#    id: Optional[str] = None
#    quantidade: int
#    entrega: bool = True
#    endereço: str
#    observacoes: Optional[str] = 'Sem Observações'
    