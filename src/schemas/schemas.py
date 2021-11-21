from pydantic import BaseModel
from typing import List, Optional
from src.infra.sqlalchemy.models.models import Produto

        
class ProdutoSimples(BaseModel):
    nome: str
    preco: float
            
    class Config:
        orm_mode = True
        
class UsuarioSimples(BaseModel):
    nome: str
    telefone: str 
    produtos: List[ProdutoSimples] = []
    
    class Config:
        orm_mode = True 
        
class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str 
    senha: str
    produtos: List[ProdutoSimples] = []
    
    class Config:
        orm_mode = True  
     
class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhe: str
    preco: float
    disponivel: bool = False
    tamanho: str
    usuario_id: Optional[int]
    usuario: Optional[Usuario]
            
    class Config:
        orm_mode = True
            
    
class Pedido(BaseModel):
    id: Optional[int] = None
    quantidade: int
    local_entrega: Optional[str]
    tipo_entrega: str
    observacao: Optional[str] = 'Sem Observações'
    usuario_id: Optional[int]
    produto_id: Optional[int]
    
    usuario: Optional[UsuarioSimples]
    produto: Optional[ProdutoSimples]
    
    class Config:
        orm_mode = True