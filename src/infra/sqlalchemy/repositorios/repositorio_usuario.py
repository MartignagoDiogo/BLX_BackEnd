from pydantic.main import prepare_config
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import select


class RepositorioUsuario():
    
    def __init__(self, session: Session):
        self.session = session
    
    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(nome = usuario.nome,
                                    telefone = usuario.telefone,
                                    senha = usuario.senha)
        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)
        return db_usuario
    
    
    def listar(self):
        usuarios = self.session.query(models.Usuario).all()
        return usuarios
    
    def listar1(self):
        stmt = select(models.Usuario)
        usuarios = self.session.execute(stmt).scalars().all()
        return usuarios
    
    def buscarPorId(self, id: int):
        consulta= select(models.Usuario).where(models.Usuario.id == id)   
        usuario= self.session.execute(consulta).first()
        return usuario  
    
    def obter_por_telefone(self, telefone) -> models.Usuario:
        query =  select(models.Usuario).where(models.Usuario.telefone == telefone)
        return self.session.execute(query).scalars().first()