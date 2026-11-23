# /plugin-authoring: descrição completa

Categoria: Criação e referência. Tipo: skill de plugin embutido do Claude Code.

## O que faz
Uma skill para fazer um "mod": uma mudança na interface ou no comportamento do Claude, como tema, painel ao lado do chat, faixa, linha de status, aviso, comando de barra ou hook em chamadas de ferramenta.

## Por que usar
Cada tipo de mod tem seu formato e seus cuidados. A skill reúne o necessário para você criar, mudar ou depurar um sem descobrir tudo por tentativa.

## Como usar
Digite /plugin-authoring com o que o mod deve fazer. Serve também para consertar um mod ou o módulo de hooks dele.

## Quando usar
Quando você quer mudar a interface ou o comportamento do próprio Claude, como um painel, uma linha de status ou um hook, e não sabe por onde começar.

## Observação
Exige a versão 2.1.287 ou mais nova.

## O que acontece no fluxo do prompt e do motor
1. Você digita /plugin-authoring.
2. Você descreve o mod.
3. A skill guia o formato e os cuidados de cada tipo.
4. O mod é criado ou consertado.
5. O mod sai criado, mudado ou depurado.

## Exemplos
- /plugin-authoring uma linha de status com a hora do último commit: cria um mod de linha de status.
- /plugin-authoring um comando /hoje que lista as tarefas abertas: cria um comando de barra novo.
- /plugin-authoring meu hook não dispara antes das chamadas do Bash: depura um hook existente.

## Comandos relacionados
- /design-sync: Enviar seu design system ao Claude Design. O card não cita outro comando; a ligação segue o critério E8 (mesma categoria).

## Armadilhas
- Descobrir tudo por tentativa.
- Esquecer o formato de cada tipo.

Documentação: https://code.claude.com/docs/en/plugins/mods/create#ask-claude-for-a-mod
