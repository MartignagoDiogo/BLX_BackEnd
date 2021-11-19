from pydantic.main import prepare_config
from sqlalchemy.orm import Session
from schemas import schemas
from infra.sqlalchemy.models import models


class RepositorioUsuario():
    
    def __init__(self, db: Session):
        self.db = db
    
    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(nome = usuario.nome,
                                    telefone = usuario.telefone)
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario
    
    
    def listar(self):
        usuarios = self.db.query(models.Usuario).all()
        return usuarios