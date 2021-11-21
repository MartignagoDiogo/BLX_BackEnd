from pydantic.schema import schema
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from typing import List

class RepositorioPedido():
    
    def __init__(self, session: Session):
        self.session = session
    
    
    def gravar_pedido(self, pedido: schemas.Pedido):
        db_pedido = models.Pedido(quantidade = pedido.quantidade,
                                  tipo_entrega = pedido.tipo_entrega,
                                  local_entrega = pedido.local_entrega,
                                  observacao = pedido.observacao,
                                  usuario_id = pedido.usuario_id,
                                  produto_id = pedido.produto_id          
                                 )
        
        self.session.add(db_pedido)
        self.session.commit()
        self.session.refresh(db_pedido)
        return db_pedido
    
    def buscar_pedido(self):
        pass
    
    def listar_meus_pedidos_id(self):
        pass

    def listar_minhas_vendas_id(self):
        pass