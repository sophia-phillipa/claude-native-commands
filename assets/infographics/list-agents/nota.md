# /list-agents: descrição completa

Categoria: Extensões e conexões. Tipo: comando embutido do Claude Code, com apelido /peers.

## O que faz
Lista os subagentes, colegas de equipe e outras sessões do Claude para os quais você pode mandar mensagem.

## Por que usar
Mostra os nomes certos antes de enviar algo e quem está disponível agora.

## Como usar
Rode /list-agents sem parâmetros.

## Quando usar
Antes de mandar mensagem para outra sessão ou subagente, para conferir quem está disponível e com que nome.

## Observação
Depende do recurso de mensagens entre sessões estar ligado na conta. Ele estava na lista do modo Desktop. A documentação descreve o uso no terminal; no Desktop dá para pedir a lista em linguagem natural.

## O que acontece no fluxo do prompt e do motor
1. Você digita /list-agents.
2. O motor reúne subagentes e sessões.
3. Você vê quem recebe mensagem.

## Exemplos
- /list-agents: Lista quem pode receber mensagem.
- /peers: Mesmo comando pelo apelido.
- /list-agents: Rode depois de abrir uma sessão paralela para ver se ela já aparece.

## Comandos relacionados
- /mcp: gerenciar servidores MCP.

## Armadilhas
- Depende do recurso de mensagens entre sessões ligado na conta.
- Sessões na nuvem exigem Remote Control.

Documentação: https://code.claude.com/docs/en/cross-session-messaging#availability
