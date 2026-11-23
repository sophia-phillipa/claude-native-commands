# /agents: descrição completa

Categoria: Automação. Tipo: comando embutido do Claude Code.

## O que faz
Na versão atual, o assistente de /agents foi removido. O comando só imprime um lembrete para pedir ao Claude que crie ou gerencie subagentes, ou para editar os arquivos em .claude/agents/ ou ~/.claude/agents/. Até a v2.1.197, ele abria uma interface interativa para configurar subagentes.

## Por que usar
Mostra o caminho que funciona hoje: pedir na conversa ou editar o arquivo direto, em vez de procurar um assistente que não existe mais.

## Como usar
No app Desktop, /agents responde que o assistente foi removido. Peça ao Claude, na conversa, o subagente que você quer, ou edite o arquivo dele em .claude/agents/.

## Quando usar
Quando você quer um subagente especializado para uma parte do trabalho. Como o assistente foi removido, a forma atual é pedir na conversa ou editar o arquivo do subagente.

## Observação
Testado no app Desktop (22/11/2026): responde "The /agents wizard has been removed.". Na referência oficial, o comando imprime um lembrete; até a v2.1.197 abria uma interface.

## O que acontece no fluxo do prompt e do motor
1. Você digita /agents
2. O motor imprime um lembrete
3. Você pede o subagente
4. Subagente criado ou editado

## Exemplos
- /agents: no app, responde que o assistente foi removido. No terminal, a referência oficial diz que ele imprime um lembrete.
- crie um subagente em .claude/agents/ que revise os testes: o caminho de hoje: o pedido vai direto na conversa, sem comando.
- mostre os subagentes deste projeto e o que cada um faz: também na conversa: o Claude lê .claude/agents/ e ~/.claude/agents/ e resume.

## Comandos relacionados
- /goal: trabalhar até a meta ser cumprida.

## Armadilhas
- O assistente foi removido.
- Versões antigas abriam uma interface.

Documentação: https://code.claude.com/docs/en/commands#all-commands
