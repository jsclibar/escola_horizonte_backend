
// Busca os elementos do HTML.
const botao = document.getElementById("cadastrar");
const resultado = document.getElementById("resultado");

// Executa quando o botão é clicado.
botao.onclick = async function () {

  // Obtém os valores digitados.
  const titulo = document.getElementById("titulo").value;
  const autor = document.getElementById("autor").value;
  const ano = Number(document.getElementById("ano").value);

  // Verifica se os campos foram preenchidos.
  if (titulo.trim() === "" || autor.trim() === "" ||
      !Number.isInteger(ano) || ano <= 0) {
    resultado.textContent = "Preencha os campos corretamente.";
    return;
  }

  // Cria um objeto JavaScript com os dados.
  const livro = {
    titulo: titulo,
    autor: autor,
    ano: ano
  };

  resultado.textContent = "Cadastrando livro...";

  try {
    // Envia os dados para a API.
    const resposta = await fetch("http://127.0.0.1:8000/livros", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(livro)
    });

    // Verifica se houve erro HTTP.
    if (resposta.ok === false) {
      throw new Error("Erro HTTP: " + resposta.status);
    }

    resultado.textContent = "Livro cadastrado com sucesso!";

  } catch (erro) {
    resultado.textContent = "Não foi possível cadastrar o livro.";
    console.error(erro);
  }
};
