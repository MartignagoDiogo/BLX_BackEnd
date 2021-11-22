from fastapi import status, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Usuario, UsuarioSimples
from src.infra.Providers import hash_provider

route = APIRouter()


@route.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UsuarioSimples)
def signup(usuario: Usuario, session: Session = Depends(get_db)):
    #verificar se ja existe um por telefone
    usuario_localizado = RepositorioUsuario(session).obter_por_telefone(usuario.telefone)
    if usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Já existe um usuário para esse telefone')
     
    usuario.senha = hash_provider.gerar_hash(usuario.senha)
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