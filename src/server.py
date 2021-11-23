from fastapi import FastAPI, requests
from fastapi.middleware.cors import CORSMiddleware
from starlette import responses
from starlette.requests import Request
from src.routers import route_auth, route_pedido, route_produto

app = FastAPI()

#CORS

origins = [
    "http://localhost:3000",
    "https://localhost:3000",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])



#Middleware

@app.middleware('http')
async def processar_tempo_requisicao(request: Request, next):
    print('chegada')
    
    response = await next(request)
    
    print('Volta')
    
    return response 
    

#Roters Produto

app.include_router(route_produto.route)

#Roters Segurança: Autenticação e Autorização

app.include_router(route_auth.route, prefix="/auth")

#Roters Pedido

app.include_router(route_pedido.router)

#ROTAS Exemplo

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
