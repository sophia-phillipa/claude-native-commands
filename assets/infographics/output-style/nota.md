# /output-style: descrição completa

Categoria: Ajustes e permissões. Tipo: comando embutido do Claude Code.

## O que faz
Lista os estilos de resposta disponíveis ou troca para um deles.

## Por que usar
O estilo muda como o Claude escreve para você. O Concise, por exemplo, corta a narração; o Explanatory e o Learning explicam mais.

## Como usar
Use /output-style sozinho para ver a lista, ou com o nome do estilo para trocar.

Parâmetro opcional: [estilo]. O nome de um estilo da lista. Sem nome, o comando só lista.

## Quando usar
Quando você quer outro jeito de resposta por um tempo, por exemplo mais explicação ao aprender algo novo, e depois voltar ao estilo curto.

## Observação
A documentação do Desktop sugere definir o outputStyle nas configurações.

## O que acontece no fluxo do prompt e do motor
1. Você digita /output-style com estilo.
2. O motor grava o estilo.
3. Próxima mensagem usa o estilo.

## Exemplos
- /output-style: mostra os estilos disponíveis.
- /output-style Concise: respostas curtas e diretas.
- /output-style: rode depois de criar um estilo seu para ver se ele entrou na lista.

## Comandos relacionados
- /config: mudar uma configuração pelo nome.

## Armadilhas
- Não obriga a seguir, é só instrução.
- Explanatory e Learning ficam mais longos.

Documentação: https://code.claude.com/docs/en/output-styles#change-your-output-style
