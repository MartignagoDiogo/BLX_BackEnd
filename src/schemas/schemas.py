from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    ip: Optional[str] = None
    nome: str
    telefone: str 
    
class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhe: str
    preco: float
    disponivel: bool = False
        
    class Config:
        orm_mode = True
            
    
#class Pedido(BaseModel):
#    id: Optional[str] = None
#    quantidade: int
#    entrega: bool = True
#    endereço: str
#    observacoes: Optional[str] = 'Sem Observações'
    