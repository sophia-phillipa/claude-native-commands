# /fewer-permission-prompts: descrição completa

Categoria: Ajustes e permissões. Tipo: skill embutida do Claude Code.

## O que faz
Lê as suas transcrições, acha os comandos Bash e MCP só de leitura que você mais aprova e grava uma allowlist priorizada no .claude/settings.json do projeto.

## Por que usar
Corta as interrupções repetidas de “posso rodar isso?” sem liberar comandos que alteram coisas.

## Como usar
Rode /fewer-permission-prompts na pasta do projeto.

Parâmetro opcional: [instruções], texto livre. Vai como argumento para a skill.

## Quando usar
Quando você se pega aprovando os mesmos comandos de leitura, como git status, rg ou ls, toda hora num projeto que usa sempre.

## O que acontece no fluxo do prompt e do motor
1. Você roda /fewer-permission-prompts.
2. O Claude lê as transcrições.
3. Acha os comandos de leitura.
4. Grava a allowlist priorizada.
5. Menos pedidos de permissão.

## Exemplos
- /fewer-permission-prompts: allowlist sugerida a partir do seu histórico.
- /fewer-permission-prompts considere só git, rg e jq: limita a lista aos comandos que você citar.
- /fewer-permission-prompts não inclua nada de MCP: fica só com comandos Bash.

## Comandos relacionados
- /config: Mudar uma configuração pelo nome.

## Armadilhas
- Só comandos de leitura entram na lista.
- Vale só para o projeto atual.

Documentação: https://code.claude.com/docs/en/commands#all-commands
