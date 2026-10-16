# Importa o FastAPI, framework usado para criar a API
# HTTPException é usado para retornar erros HTTP
from fastapi import FastAPI, HTTPException

# Importa o BaseModel do Pydantic
# Ele será usado para definir e validar os dados recebidos pela API
from pydantic import BaseModel

# Importa o Uvicorn, servidor responsável por executar a aplicação
import uvicorn


# Cria a aplicação FastAPI e define as informações da documentação
app = FastAPI(
    title="Backend (API) da Escola Horizonte",
    description="API para gerenciamento do backend da Escola Horizonte",
    version="1.0.0"
)


# Define o modelo dos dados esperados para um aluno
# O nome e o email são obrigatórios e devem ser textos
class Aluno(BaseModel):
    nome: str
    email: str


# Lista de alunos armazenada em memória
# Compartilhada entre os endpoints da API
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

# Controla o ID do próximo aluno
proximo_id = 3


# Endpoint GET /
# Retorna uma mensagem simples para verificar se a API está funcionando
@app.get("/", tags=["Geral"], summary="Hello World")
def home():
    return {"message": "Hello World"}


# Endpoint GET /alunos
# Retorna a lista de todos os alunos
@app.get("/alunos", tags=["Alunos"], summary="Listar alunos")
def listar_alunos():
    return alunos


# Endpoint GET /alunos/{idaluno}
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


# Endpoint POST /alunos
# Recebe os dados de um novo aluno através do corpo (body) da requisição
@app.post(
    "/alunos",
    tags=["Alunos"],
    summary="Cadastrar aluno",
    status_code=201
)
def cadastrar_aluno(aluno: Aluno):

    global proximo_id

    # Cria um novo aluno
    novo_aluno = {
        "idaluno": proximo_id,
        "nome": aluno.nome,
        "email": aluno.email
    }

    # Adiciona o aluno à lista
    alunos.append(novo_aluno)

    # Incrementa o ID para o próximo cadastro
    proximo_id += 1

    return {
        "message": "Aluno cadastrado com sucesso",
        "aluno": novo_aluno
    }


# Endpoint PUT /alunos/{idaluno}
# Recebe o ID do aluno e os novos dados através do corpo (body) da requisição
@app.put(
    "/alunos/{idaluno}",
    tags=["Alunos"],
    summary="Atualizar aluno",
    responses={
        404: {"description": "Aluno não encontrado"}
    }
)
def atualizar_aluno(idaluno: int, dados: Aluno):

    # Percorre a lista procurando o aluno pelo ID
    for aluno in alunos:
        if aluno["idaluno"] == idaluno:

            # Atualiza os dados do aluno
            aluno["nome"] = dados.nome
            aluno["email"] = dados.email

            return {
                "message": "Aluno atualizado com sucesso",
                "aluno": aluno
            }

    # Se o aluno não for encontrado, lança uma exceção HTTP
    raise HTTPException(
        status_code=404,
        detail="Aluno não encontrado"
    )


# Endpoint DELETE /alunos/{idaluno}
# Recebe o ID do aluno que será excluído
@app.delete(
    "/alunos/{idaluno}",
    tags=["Alunos"],
    summary="Excluir aluno",
    responses={
        404: {"description": "Aluno não encontrado"}
    }
)
def excluir_aluno(idaluno: int):

    # Percorre a lista procurando o aluno pelo ID
    for aluno in alunos:
        if aluno["idaluno"] == idaluno:

            # Remove o aluno da lista
            alunos.remove(aluno)

            return {
                "message": "Aluno excluído com sucesso",
                "idaluno": idaluno
            }

    # Se o aluno não for encontrado, lança uma exceção HTTP
    raise HTTPException(
        status_code=404,
        detail="Aluno não encontrado"
    )


# Executa o servidor Uvicorn somente quando este arquivo é iniciado diretamente
if __name__ == "__main__":
    uvicorn.run(
        "05-alunos_put_fastapi:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
