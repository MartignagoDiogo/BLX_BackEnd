from fastapi import status, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Usuario, UsuarioSimples

route = APIRouter()


@route.post('/signup', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuarios(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@route.get('/usuarios', status_code=status.HTTP_200_OK, response_model=List[UsuarioSimples])
def listar_usuarios(session: Session = Depends(get_db)):
    usuario = RepositorioUsuario(session).listar()
    return usuario

@route.get('/usuarios/{id}')
def exibir_usuario(id: int, session: Session = Depends(get_db)):
    usuario_localizado = RepositorioUsuario(session).buscarPorId(id)
    if not usuario_localizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'não existe o usuario com o id = {id}')
    return usuario_localizado