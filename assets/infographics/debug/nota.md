# /debug: descrição completa

Categoria: Diagnóstico e uso. Tipo: skill embutida do Claude Code.

## O que faz
Liga o registro detalhado desta sessão e ajuda a investigar um problema. Ele só lê arquivos e registros, sem alterar nada.

## Por que usar
Mostra o que de fato aconteceu num hook, num MCP ou num comando que falhou, em vez de adivinhar.

## Como usar
Use /debug com a descrição do problema. Só você consegue chamar: o Claude não o dispara sozinho.

Parâmetro opcional: [descrição], texto livre. O que deu errado, com o máximo de detalhe.

## Quando usar
Quando um hook, um MCP ou um comando se comporta diferente do esperado e você quer o registro detalhado do que acontece a partir de agora.

## Observação
O registro começa quando você roda o comando: o que aconteceu antes não fica gravado. Rode e repita o que falhou.

## O que acontece no fluxo do prompt e do motor
1. Você digita /debug.
2. O motor liga o registro detalhado da sessão.
3. O motor lê o registro.
4. O motor analisa a falha, com a descrição que você deu.
5. O resultado mostra o que falhou.

## Exemplos
- /debug o MCP context7 não conecta desde que abri a sessão: investiga uma conexão que falha.
- /debug um hook está deixando cada comando mais lento: procura o que está atrasando.
- /debug o /skill-doctor diz que não está disponível nesta conexão: investiga um comando que responde indisponível no app.

## Comandos relacionados
- /skill-doctor: mostra as skills que pesam no contexto.

## Armadilhas
- Falhas anteriores não ficam gravadas.

Documentação: https://code.claude.com/docs/en/skills#bundled-skills
