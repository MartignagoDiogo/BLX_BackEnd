from fastapi import APIRouter, status, Depends
from typing import List
from src.schemas.schemas import Produto, ProdutoSimples
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto



route = APIRouter()

#ROTAS PRODUTOS

@route.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[ProdutoSimples])
def listar_produtos(session: Session = Depends(get_db)):
    produtos = RepositorioProduto(session).listar()
    return produtos

@route.post('/produtos', status_code=status.HTTP_200_OK)
def criar_produtos(produto: Produto, session: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado


@route.put('/produtos/{id}', response_model=ProdutoSimples)
def atualizar_produtos(id: int, produto: Produto, session: Session = Depends(get_db)):
        RepositorioProduto(session).editar(id, produto)
        produto.id = id
        return produto
    
@route.delete('/produtos/{id}')   
def remover_produtos(id: int, session: Session = Depends(get_db)):
        RepositorioProduto(session).remover(id)
        return 'Produto removido'

