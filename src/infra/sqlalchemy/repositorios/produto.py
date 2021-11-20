from pydantic.main import prepare_config
from sqlalchemy.orm import Session
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
    
    def remover(self):
        pass
    
