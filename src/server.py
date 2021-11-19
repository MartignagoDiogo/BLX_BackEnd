from fastapi import FastAPI, Depends, status
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm.session import Session
from infra.sqlalchemy.config.database import get_db, criar_db
from schemas.schemas import ProdutoSimples, Usuario, Produto
from infra.sqlalchemy.repositorios.produto import RepositorioProduto
from infra.sqlalchemy.repositorios.usuario import RepositorioUsuario


criar_db()

app = FastAPI()


@app.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[ProdutoSimples])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@app.post('/produtos', status_code=status.HTTP_200_OK)
def criar_produtos(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.post('/usuario', status_code=status.HTTP_201_CREATED)
def criar_usuarios(usuario: Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado

@app.get('/usuarios', status_code=status.HTTP_200_OK)
def listar_usuarios(db: Session = Depends(get_db)):
    usuario = RepositorioUsuario(db).listar()
    return usuario










@app.get('/')
async def roo():
    return {'Fala ai Bradipo'}

@app.get('/profile/{nome}')
async def signup(nome: str):
    return {f'A casa esta feita, {nome}'}

@app.get('/profile')
async def profile():
    return {'Aqui é a casa do Bradipo'}

@app.put('/profile')
async def atualizar():
    return {'Casa reformada'}

@app.delete('/profile')
async def remover():
    return {'Aqui é a casa do Bradipo'}

@app.get("/quadrado/{numero}")
async def quadrado(numero: int):
    r = numero * numero
    return {f'O quadrado de {numero} é {r}'}

@app.get('/dobro')
def dobro(valor: int = 1):
    r = 2 * valor
    return {f'O dobro de {valor} é {r}' }
