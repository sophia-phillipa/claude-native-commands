# /insights: descrição completa

Categoria: Diagnóstico e uso. Tipo: comando embutido do Claude Code.

## O que faz
Analisa as sessões de todos os projetos desta máquina, não só do projeto aberto, e gera um relatório que pode ser compartilhado.

## Por que usar
Dá uma visão do seu uso ao longo de vários projetos e sessões, que uma sessão sozinha não mostra.

## Como usar
Rode /insights sem parâmetros, de qualquer projeto: o resultado é o mesmo. Só você consegue chamar: o Claude não o dispara sozinho.

## Quando usar
No fim de uma semana ou de um mês, para ver o seu uso em todos os projetos de uma vez e decidir o que vale automatizar.

## Observação
Ele lê a pasta ~/.claude/projects inteira, das sessões mais recentes para as mais antigas. Guarda o que já analisou e, a cada rodada, analisa até cerca de 200 sessões novas, então a primeira vez demora mais. O relatório mais recente fica em ~/.claude/usage-data/report.html, e cada rodada guarda uma cópia com data. Sessões de outros aparelhos e do claude.ai não entram.

## O que acontece no fluxo do prompt e do motor
1. Você digita /insights.
2. O motor lê as sessões da máquina.
3. O motor analisa só as sessões ainda não vistas.
4. O motor monta o relatório em HTML.
5. O relatório HTML fica salvo em ~/.claude/usage-data.

## Exemplos
- /insights: gera o relatório das suas sessões.
- /insights: rode no fim da semana e compare com o relatório anterior.
- /insights: rode depois de um mês com um fluxo novo para ver se ele mudou o seu uso.

## Comandos relacionados
- /doctor: check-up da instalação.

## Armadilhas
- A primeira rodada demora mais.
- Não inclui sessões de outros aparelhos.

Documentação: https://code.claude.com/docs/en/costs#analyze-your-usage-patterns
