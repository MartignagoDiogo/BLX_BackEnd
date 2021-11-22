from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])

def verificar_hash(tesxto_plano, texto_hash):
    return pwd_context.verify(tesxto_plano, texto_hash)

def gerar_hash(texto_plano):
    return pwd_context.hash(texto_plano)