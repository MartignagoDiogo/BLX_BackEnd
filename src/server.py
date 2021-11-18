from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


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