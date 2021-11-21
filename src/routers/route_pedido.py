from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from src.infra.sqlalchemy.config.database import get_db
from sqlalchemy.orm import Session
from src.schemas.schemas import Pedido, ProdutoSimples
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido

router = APIRouter()

@router.post('/pedido', status_code=status.HTTP_201_CREATED, response_model=Pedido)
def fazer_pedido(pedido: Pedido, session: Session = Depends(get_db)):
    pedido_criado = RepositorioPedido(session).gravar_pedido(pedido)
    return pedido_criado

@router.get('/pedido/{id}', status_code=status.HTTP_200_OK, response_model=Pedido)
def exibir_pedido(id: int, session: Session = Depends(get_db)):
    pedido = RepositorioPedido(session).buscar_pedido(id)
    return pedido

@router.get('/pedido', status_code=status.HTTP_200_OK, response_model=List[Pedido])
def listar_pedido(session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(session).listar_meus_pedidos_id()
    return pedidos

@router.get('/pedido/{usuario_id}/vendas', status_code=status.HTTP_200_OK, response_model=List[Pedido])
def listar_venda(usuario_id: int, session: Session = Depends(get_db)):
    vendas = RepositorioPedido(session).listar_minhas_vendas_id(usuario_id)
    return vendas