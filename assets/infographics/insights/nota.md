# /insights: descrição completa

Categoria: Diagnóstico e uso. Tipo: comando embutido do Claude Code.

## O que faz
Analisa as sessões de todos os projetos desta máquina, não só do projeto aberto, e gera um relatório em HTML.

## Por que usar
Dá uma visão do seu uso ao longo de vários projetos e sessões, que uma sessão sozinha não mostra.

## Como usar
Rode /insights sem parâmetros, de qualquer projeto: o resultado é o mesmo. Só você consegue chamar: o Claude não o dispara sozinho.

## Quando usar
No fim de uma semana ou de um mês, para ver o seu uso em todos os projetos de uma vez e decidir o que vale automatizar.

## Observação
Ele analisa as sessões desta máquina que ainda não viu, até cerca de 200 por rodada, e pula as muito curtas. Guarda o que já analisou, então a primeira vez demora mais.

## O que acontece no fluxo do prompt e do motor
1. Você digita /insights
2. O motor lê as sessões
3. Analisa sessões ainda não vistas
4. Monta o relatório em HTML
5. Relatório HTML fica salvo

## Exemplos
- /insights: Gera o relatório das suas sessões.
- /insights: Rode no fim da semana e compare com o relatório anterior.
- /insights: Rode depois de um mês com um fluxo novo para ver se ele mudou o seu uso.

## Comandos relacionados
- /doctor: Check-up da instalação.

## Armadilhas
- A primeira rodada demora mais.
- Não inclui sessões de outros aparelhos.
</content>
