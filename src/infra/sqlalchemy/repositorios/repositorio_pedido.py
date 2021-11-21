from pydantic.schema import schema
from sqlalchemy.orm import Session, query
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.functions import mode
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
    
    def buscar_pedido_por_id(self, id: int):
        query = select(models.Pedido).where(models.Pedido.id == id)
        pedido = self.session.execute(query).one()
        return pedido
    
    def listar_meus_pedidos_id(self, usuario_id: int):
        query = select(models.Pedido).where(models.Pedido.usuario_id == usuario_id)
        r = self.session.execute(query).all()
        return r

    def listar_minhas_vendas_id(self, usuario_id: int):
        query = select(models.Pedido).join_from(models.Pedido, models.Produto).where(models.Pedido.usuario_id == usuario_id)
        r = self.session.execute(query).all()
        return r