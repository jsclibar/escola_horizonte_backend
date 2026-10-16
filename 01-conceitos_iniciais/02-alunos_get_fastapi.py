# Importa o FastAPI, framework usado para criar a API
from fastapi import FastAPI, HTTPException

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
# Retorna a lista de todos os alunos
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


# Endpoint GET /alunos/{id}
# Retorna um aluno específico através do ID
@app.get(
    "/alunos/{idaluno}",
    tags=["Alunos"],
    summary="Buscar aluno por ID",
    responses={
        404: {"description": "Aluno não encontrado"}
    }
)
def buscar_aluno(idaluno: int):

    alunos = [
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

    # Percorre a lista procurando o aluno pelo ID
    for aluno in alunos:
        if aluno["idaluno"] == idaluno:
            return aluno

    # Se o aluno não for encontrado, lança uma exceção HTTP
    # O FastAPI transforma essa exceção em uma resposta com status 404
    raise HTTPException(
        status_code=404,
        detail="Aluno não encontrado"
    )

# Executa o servidor Uvicorn somente quando este arquivo é iniciado diretamente
if __name__ == "__main__":
    uvicorn.run(
        "02-alunos_get_fastapi:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )