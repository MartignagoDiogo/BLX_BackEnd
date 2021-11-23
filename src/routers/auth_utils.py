from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer, oauth2
from fastapi import status
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.Providers import  token_provider
from jose import JWTError
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario

from src.schemas.schemas import Usuario

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

def obter_usuario_logado(token: str = Depends(oauth2_schema), session: Session = Depends(get_db)):
    try:
        telefone = token_provider.verificar_acess_token(token)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token invalido')
    if not telefone:
        raise HTTPException(status_code=status.HTTP_402_PAYMENT_REQUIRED, detail='Token invalido')
    usuario = RepositorioUsuario(session).obter_por_telefone(telefone)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Token invalido')
    return usuario