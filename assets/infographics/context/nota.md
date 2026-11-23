# /context: descrição completa

Categoria: Contexto e memória. Tipo: comando embutido do Claude Code.

## O que faz
Mostra o uso atual da janela de contexto, com uma tabela por categoria e a lista de ferramentas MCP, agentes e skills com os tokens de cada um.

## Por que usar
Explica por que uma sessão ficou pesada e o que cortar. Com muitos servidores MCP ligados, as ferramentas deles costumam ser uma das maiores fatias.

## Como usar
Rode /context sem parâmetros. No app, o teste cobriu só a tabela por categoria; o argumento all, que expande a tabela, não foi testado.

## Quando usar
Quando as respostas ficam lentas ou a sessão parece pesada, e antes de colar um log grande. Olhe primeiro as maiores fatias da tabela: é ali que o corte rende mais.

## Observação
Testado no app: tabela por categoria.

## O que acontece no fluxo do prompt e do motor
1. Você digita /context
2. O motor soma por categoria
3. Aponta ferramentas que pesam
4. Você vê o que cortar

## Exemplos
- /context: retrato do contexto agora.
- /context: rode antes e depois de um /compact para ver quanto foi liberado.
- /context: rode depois de desligar um servidor com /mcp disable para ver a linha MCP diminuir.

## Comandos relacionados
- /compact: mostra quanto foi liberado.
- /mcp: mostra a linha MCP diminuir.

## Armadilhas
- Servidores MCP ligados costumam pesar.

Documentação: https://code.claude.com/docs/en/context-window#check-your-own-session
