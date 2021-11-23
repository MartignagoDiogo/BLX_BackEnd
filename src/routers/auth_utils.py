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
    
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token invalido')
    try:
        telefone: str = token_provider.verificar_acess_token(token)
    except JWTError:
            raise exception
        
    if not telefone:
        raise exception
    
    usuario = RepositorioUsuario(session).obter_por_telefone(telefone)
    
    if not usuario:
        raise exception
    
    return usuario