from sqlalchemy import update, delete
from pydantic.main import prepare_config
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import delete
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioProduto():
    
    def __init__(self, session: Session):
        self.session = session      
        
    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(nome=produto.nome,
                                     detalhe=produto.detalhe,
                                     preco=produto.preco,
                                     disponivel=produto.disponivel,
                                     tamanho=produto.tamanho,
                                     usuario_id=produto.usuario_id)
        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto        
        
    def listar(self):
        produtos = self.session.query(models.Produto).all()
        return produtos        
   
    def editar(self, id: int, produto: schemas.Produto):
        stmt_update = update(models.Produto).where(
            models.Produto.id == id).values(nome=produto.nome,
                                            detalhe=produto.detalhe,
                                            preco=produto.preco,
                                            disponivel=produto.disponivel,
                                            tamanho=produto.tamanho
                                            )
        self.session.execute(stmt_update)
        self.session.commit()
        return stmt_update
    
    def remover(self, id: int):
        stmt_delete = delete(models.Produto).where(models.Produto.id == id)
        
        self.session.execute(stmt_delete)
        self.session.commit()
        return stmt_delete
        