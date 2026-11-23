# /plan: descrição completa

Categoria: Modelo e potência. Tipo: comando embutido do Claude Code.

## O que faz
Entra no modo plano direto pelo prompt. Com uma descrição, entra no modo e já começa essa tarefa.

## Por que usar
Em tarefas grandes, planejar antes evita mudanças no escopo errado.

## Como usar
Rode /plan sozinho para entrar no modo, ou /plan seguido da tarefa para começar nela.

Parâmetro opcional: [description]. A tarefa a planejar; sem ela, só o modo é ativado.

## Quando usar
Antes de uma tarefa grande ou arriscada, quando vale montar o plano e revisá-lo antes de qualquer mudança.

## Observação
Documentado na referência oficial.

## O que acontece no fluxo do prompt e do motor
1. Você digita /plan.
2. O motor ativa modo plano.
3. Com descrição, começa a tarefa.
4. A sessão fica em modo plano.

## Exemplos
- /plan corrigir o bug de autenticação: entra no modo plano já com essa tarefa.
- /plan: liga o modo plano sem começar uma tarefa ainda.
- /plan migrar a tabela de usuários para o novo esquema: começa pelo plano da migração antes da execução.

## Comandos relacionados
- /model: trocar o modelo da sessão.

## Armadilhas
- Sem descrição, só o modo é ativado.

Documentação: https://code.claude.com/docs/en/commands#all-commands
