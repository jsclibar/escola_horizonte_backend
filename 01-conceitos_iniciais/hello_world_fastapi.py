# Importa o FastAPI, framework usado para criar a API
from fastapi import FastAPI

# Importa o Uvicorn, servidor responsável por executar a aplicação
import uvicorn

# Cria a aplicação FastAPI e define as informações da documentação
app = FastAPI(
    title="Backend (API) da Escola Horizonte",
    description="API para gerenciamento do backend da Escola Horizonte",
    version="1.0.0"
)


# Endpoint GET /
# Retorna uma mensagem simples para verificar se a API está funcionando
@app.get("/", tags=["Geral"], summary="Hello World")
def home():
    return {"message": "Hello World"}


# Endpoint GET /alunos
# Retorna uma lista de alunos
@app.get("/alunos", tags=["Alunos"], summary="Listar alunos")
def listar_alunos():
    return [
        {
            "idaluno": 1,
            "nome": "Maria da Silva",
            "email": "maria@email.com"
        },
        {
            "idaluno": 2,
            "nome": "Andre Santos",
            "email": "andre@email.com"
        }
    ]


# Executa o servidor Uvicorn somente quando este arquivo é iniciado diretamente
if __name__ == "__main__":
    uvicorn.run(
        "hello_world_fastapi:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
