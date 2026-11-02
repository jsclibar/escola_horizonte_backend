// Busca o botão e a lista pelos IDs definidos no HTML.
const botao = document.getElementById("buscar");
const lista = document.getElementById("livros");

// Executa a função ao clicar no botão.
// async permite usar await para aguardar a resposta da API.
botao.onclick = async function () {
  // Altera o texto exibido na lista.
  lista.textContent = "Carregando livros...";

  // try/catch trata erros, como try/except no Python.
  try {
    // Faz um GET na API e aguarda a resposta.
    const resposta = await fetch("http://127.0.0.1:8000/livros");

    // Se o status HTTP indicar erro, envia a execução para o catch.
    // throw new Error é semelhante a raise Exception no Python.
    if (resposta.ok === false) {
      throw new Error("A API não conseguiu consultar os livros.");
    }

    // Converte o JSON recebido em um array de objetos.
    // É parecido com uma lista de dicionários no Python.
    const livros = await resposta.json();

    // Limpa o conteúdo anterior da lista.
    lista.textContent = "";

    // length equivale ao len() do Python.
    if (livros.length === 0) {
      lista.textContent = "Nenhum livro encontrado.";
    }

    // Equivale a: for livro in livros:
    for (const livro of livros) {
      // Cria um item HTML para mostrar o livro.
      const item = document.createElement("li");

      // Preenche o item com os dados recebidos da API.
      item.textContent =
        livro.titulo + " — " + livro.autor + " (" + livro.ano + ")";

      // Adiciona o item à lista na página.
      lista.appendChild(item);
    }
  } catch {
    // Mostra uma mensagem se ocorrer algum erro.
    lista.textContent = "Não foi possível buscar os livros.";
  }
};