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
Depende da versão do Claude Code (2.1.224 ou mais nova; 2.1.234 no Windows nativo), do sistema, do provedor e da configuração da sessão. Para ver sessões em outras máquinas, a sessão precisa estar no Remote Control, que exige login no claude.ai. Ele estava na lista do modo Desktop. A documentação descreve o uso no terminal; no Desktop dá para pedir a lista em linguagem natural.

## O que acontece no fluxo do prompt e do motor
1. Você digita /list-agents
2. Motor reúne subagentes e sessões
3. Você vê quem recebe mensagem

## Exemplos
- /list-agents: Lista quem pode receber mensagem.
- /peers: Mesmo comando pelo apelido.
- /list-agents: Rode depois de abrir uma sessão paralela para ver se ela já aparece.

## Comandos relacionados
- /mcp: Gerenciar servidores MCP.

## Armadilhas
- Depende da versão do Claude Code.
- Sessões de outras máquinas exigem Remote Control.

Documentação: https://code.claude.com/docs/en/cross-session-messaging#availability
