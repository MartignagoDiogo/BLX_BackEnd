from fastapi import status, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.infra.Providers import token_provider
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Usuario, UsuarioSimples, LoginData
from src.infra.Providers import hash_provider
from src.routers.auth_utils import obter_usuario_logado

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

@route.post('/token')
def login(login_data: LoginData, session: Session = Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone
    
    usuario = RepositorioUsuario(session).obter_por_telefone(telefone)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='senha ou telefone estão incorretos')
    senha_valida = hash_provider.verificar_hash(senha, usuario.senha)
    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='senha ou telefone estão incorretos')
    
    #Gerar o token JWT
    token = token_provider.criar_acess_token({'sub': usuario.telefone})
    return {'usuario': usuario, 'access_token': token}

@route.get('/usuarios', status_code=status.HTTP_200_OK, response_model=List[UsuarioSimples])
def listar_usuarios(session: Session = Depends(get_db)):
    usuario = RepositorioUsuario(session).listar()
    return usuario

@route.get('/usuarios/{id}', response_model=UsuarioSimples)
def exibir_usuario(id: int, session: Session = Depends(get_db)):
    usuario_localizado = RepositorioUsuario(session).buscarPorId(id)
    if not usuario_localizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'não existe o usuario com o id = {id}')
    return usuario_localizado

@route.get('/me', response_model=UsuarioSimples)
def me(usuario: Usuario = Depends(obter_usuario_logado)):
    #decodificar o token, pegar o telefone, buscar user no BD retornar
    return usuario