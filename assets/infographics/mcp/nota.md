# /mcp: descrição completa

Categoria: Extensões e conexões. Tipo: comando embutido do Claude Code.

## O que faz
Mostra os servidores MCP da sessão e permite reconectar, ligar ou desligar cada um.

## Por que usar
Um servidor caído deixa ferramentas fora do ar. Desligar os que você não usa também libera contexto, porque as ferramentas de cada servidor ocupam espaço na janela.

## Como usar
Use /mcp sozinho ou com uma ação.

Parâmetros:
- reconnect: Reconecta um servidor que caiu ou travou.
- enable · disable: Liga ou desliga um servidor.
- <servidor> · all: O nome do servidor, ou all para todos de uma vez.

## Quando usar
Quando uma ferramenta MCP para de responder ou some, e no começo de uma sessão que não vai usar certos servidores, para liberar contexto.

## Observação
No Desktop, os conectores também têm uma tela própria; o /mcp é o caminho por comando.

## O que acontece no fluxo do prompt e do motor
1. Você digita /mcp.
2. Painel lista os servidores.
3. Reconecta ou desliga um servidor.
4. Ferramentas voltam ou param.

## Exemplos
- /mcp: Lista os servidores e o estado de cada um.
- /mcp reconnect context7: Reconecta só o context7.
- /mcp disable playwright: Desliga um servidor que esta sessão não vai usar.

## Comandos relacionados
- /context: Mostra as ferramentas MCP e tokens.

## Armadilhas
- No Desktop, conectores têm tela própria.
- Liga e desliga valem por projeto.

Documentação: https://code.claude.com/docs/en/mcp
