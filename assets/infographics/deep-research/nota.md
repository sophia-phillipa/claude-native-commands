# /deep-research: descrição completa

Categoria: Automação. Tipo: workflow embutido do Claude Code.

## O que faz
Um workflow que abre várias buscas na web sobre uma pergunta, busca as fontes, cruza as informações entre elas e sintetiza um relatório com citações.

## Por que usar
Entrega um relatório com citações, em vez de uma resposta sem referência.

## Como usar
Digite /deep-research seguido da pergunta.

Parâmetro obrigatório: <question>, a pergunta que a pesquisa deve responder.

## Quando usar
Quando a pergunta pede várias fontes da web e você precisa de um texto com citações para conferir.

## Observação
Workflow embutido listado na referência oficial de workflows.

## O que acontece no fluxo do prompt e do motor
1. Você digita /deep-research.
2. O motor busca fontes em vários ângulos.
3. O motor cruza as informações, vota cada afirmação e filtra as que não se sustentam.
4. A sessão recebe o relatório com citações.

## Exemplos
- /deep-research quais mudanças importantes saíram na última versão do SDK de Python?: busca as fontes, cruza as informações e entrega o relatório com citações.
- /deep-research comparação de preços dos planos de banco de dados gerenciado: relatório que compara as fontes encontradas, com as referências.
- /deep-research o que a documentação oficial diz sobre limites de taxa de uma API: relatório sintetizado, com as páginas consultadas citadas.

## Comandos relacionados
- /goal: trabalhar até a meta ser cumprida.

## Armadilhas
- Afirmação sem checagem fica não verificada no relatório, em vez de ser contada como refutada.
- Exige busca na web disponível.

Documentação: https://code.claude.com/docs/en/workflows#bundled-workflows
