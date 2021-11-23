from datetime import timedelta, datetime
from jose import jwt


#CONFIG 
SECRET_KEY = '162cb1a1c7702e21363d5168e4765bed'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000


def criar_acess_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(EXPIRES_IN_MIN)
    
    dados.update({'exp': expiracao})
    
    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt

def verificar_acess_token(token: str):
    carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return carga.get('sub')