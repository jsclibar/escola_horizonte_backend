from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Backend (API) da Escola Horizonte",
    description="API para gerenciamento do backend da Escola Horizonte",
    version="1.0.0"
)


@app.get("/", tags=["Geral"], summary="Hello World")
def home():
    return {"message": "Hello World"}


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

if __name__ == "__main__":
    uvicorn.run(
        "hello_world_fastapi:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
