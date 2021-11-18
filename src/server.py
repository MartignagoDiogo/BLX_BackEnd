from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm.session import Session
from infra.sqlalchemy.config.database import get_db, criar_db
from schemas.schemas import Produto
from infra.sqlalchemy.repositorios.produto import RepositorioProduto


criar_db()
app = FastAPI()


@app.get('/produtos')
def listar_produtos():
    return {'listou'}

@app.post('/produtos')
async def criar_produtos(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto().criar(produto)
    return produto_criado













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

class Usuario(BaseModel):
    nome: str
    valor: float

@app.post('/user')
def usuario(user: Usuario):
    return { f'Usuario {user.nome} - camisa {user.valor} cadastrado com sucesso'}