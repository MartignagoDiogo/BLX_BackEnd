from pydantic import BaseModel
from typing import Optional

class Usuario():
    ip: Optional[str] = None
    nome: str
    telefone: str 
    
class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhe: str
    disponivel: bool = False
    
class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereço: str
    observacoes: Optional[str] = 'Sem Observações'
    