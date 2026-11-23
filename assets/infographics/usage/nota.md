# /usage: descrição completa

Categoria: Diagnóstico e uso. Tipo: comando embutido do Claude Code.

## O que faz
Mostra o custo da sessão, o uso do seu plano e o que mais está consumindo os seus limites.

## Por que usar
Ajuda a decidir quando trocar de modelo, baixar o esforço ou compactar antes de bater no limite.

## Como usar
Rode /usage sem parâmetros. /cost é apelido do mesmo comando. Na documentação, /stats é atalho de /usage; no app ele aparece como comando próprio.

## Quando usar
Antes de começar algo caro, como um /batch ou um /code-review max, e no meio de uma semana de uso pesado, para saber quanto ainda resta do plano.

## Observação
Em planos Pro, Max, Ultra, Team ou Enterprise, a documentação do plano mostra a atribuição do uso a skills, subagentes, plugins e servidores MCP, cada um com a sua porcentagem do total. Os números são aproximados e vêm do histórico local desta máquina.

## O que acontece no fluxo do prompt e do motor
1. Você digita /usage.
2. O motor soma o custo da sessão.
3. O motor atribui o uso às fontes: skills, subagentes, plugins e servidores MCP.
4. O motor calcula a porcentagem de cada fonte.
5. O painel mostra o que mais consome o plano.

## Exemplos
- /usage: painel de custo e limites.
- /cost: mesmo comando pelo apelido.
- /usage: antes de um /batch ou de um /code-review max, para ver quanto do plano ainda resta.

## Comandos relacionados
- /batch: executa uma mudança grande em paralelo.
- /code-review: caça bugs no diff atual.

## Armadilhas
- Não inclui uso de outros aparelhos.
- Custo da sessão não vale para cobrança.

Documentação: https://code.claude.com/docs/en/costs#plan-usage-breakdown
