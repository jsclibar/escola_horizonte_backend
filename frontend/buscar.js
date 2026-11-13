
// Busca os elementos do HTML.
const botao = document.getElementById("buscar");
const codigo = document.getElementById("codigo");
const resultado = document.getElementById("resultado");

// Executa quando o botão é clicado.
botao.onclick = async function () {

  // Obtém o ID digitado.
  const id = codigo.value;

  if (id === "" || Number(id) < 1 || !Number.isInteger(Number(id))) {
    resultado.textContent = "Digite um ID válido.";
    return;
  }

  resultado.textContent = "Buscando livro...";

  try {
    // Faz a requisição GET com o ID informado.
    const resposta = await fetch(
      "http://127.0.0.1:8000/livros/" + id
    );

    // Verifica se o livro foi encontrado.
    if (resposta.status === 404) {
      resultado.textContent = "Livro não encontrado.";
      return;
    }

    // Verifica outros erros HTTP.
    if (resposta.ok === false) {
      throw new Error();
    }

    // Converte o JSON em objeto JavaScript.
    const livro = await resposta.json();

    // Mostra os dados do livro.
    resultado.textContent =
      livro.titulo + " — " +
      livro.autor + " (" +
      livro.ano + ")";

  } catch {
    resultado.textContent =
      "Não foi possível buscar o livro.";
  }
};
