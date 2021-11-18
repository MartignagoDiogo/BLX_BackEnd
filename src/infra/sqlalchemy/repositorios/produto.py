from pydantic.main import prepare_config
from sqlalchemy.orm import Session
from schemas import schemas
from infra.sqlalchemy.models import models


class RepositorioProduto():
    def __init__(self, db: Session):
        self.db = db
        
    def criar(self, produto: schemas.Produto):
        db_produto = models.Produtos(nome=produto.nome,
                                     detalhes=produto.detalhes,
                                     preco=produto.preco,
                                     disponivel=produto.disponivel)
        self.db.add(db_produto)
        self.db.comit()
        self.db.refresh(db_produto)
        return db_produto
        
        
    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos
    
    def remover(self):
        pass
    
