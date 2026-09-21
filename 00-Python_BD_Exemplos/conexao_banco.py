# Importa o módulo mysql.connector para conectar ao banco de dados MySQL
import mysql.connector

# Variável que armazenará a conexão com o banco
# Inicialmente, a conexão é None, indicando que ainda não foi estabelecida
conexao = None
cursor = None

# O try é o bloco que será executado, e caso ocorra algum 
# erro, o bloco except será acionado
try:
    # Parametros de conexão com o banco de dados MySQL
    conexao = mysql.connector.connect(
        host="127.0.0.1", # ou localhost
        port=3306, # Porta padrão do MySQL
        user="root", # Usuário do banco de dados
        password="root", # Senha do usuário do banco de dados
        database="escola_horizonte" # Nome do banco de dados que será acessado
    )

    # Verifica se a conexão foi realizada
    if conexao.is_connected():
        print("Conexão realizada com sucesso!\n")

        # O cursor é o objeto que permite executar comandos SQL no banco de dados
        # O parâmetro dictionary=True faz com que os resultados das consultas 
        # # sejam retornados como dicionários, facilitando o acesso aos dados 
        # pelas chaves (nomes das colunas)
        cursor = conexao.cursor(dictionary=True)

        # Executa uma consulta no banco
        cursor.execute("SELECT * FROM ALUNO")

        # Armazena os registros retornados pela consulta em uma variável
        alunos = cursor.fetchall()

        # Exibe os registros na tela
        print("Lista de alunos:")
        print()

        # Percorre a lista de alunos e exibe os detalhes de cada um
        for aluno in alunos:
            print(f"ID: {aluno['idaluno']}")
            print(f"Nome: {aluno['nome']}")
            print(f"E-mail: {aluno['email']}")
            print(f"Idade: {aluno['idade']}")
            print("----------------------------")

# Se o bloco try gerar algum erro, o bloco except será executado
except mysql.connector.Error as e: # Captura o erro gerado pelo MySQL e armazena na variável 'e'
    print(f"Erro ao acessar o banco de dados: {e}")

finally: # O bloco finally é executado independentemente de ocorrer um erro ou não, garantindo que recursos sejam liberados
    # Fecha o cursor, caso tenha sido criado
    if cursor is not None:
        cursor.close()

    # Fecha a conexão com o banco
    if conexao is not None and conexao.is_connected():
        conexao.close()
        print("\nConexão encerrada.")
