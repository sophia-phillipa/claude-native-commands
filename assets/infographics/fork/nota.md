# /fork: descrição completa

Categoria: Modelo e potência. Tipo: comando embutido do Claude Code.

## O que faz
Copia a conversa atual para uma nova sessão em segundo plano e deixa você continuar aqui. Com um prompt, a cópia começa a trabalhar nele logo de início; sem prompt, espera o primeiro na visão de agentes. Salvo quando a cópia edita no lugar, o Claude Code manda ela criar um worktree próprio antes de alterar código.

## Por que usar
Permite tentar outra abordagem ou deixar uma tarefa correndo sem perder o contexto já montado nesta conversa.

## Como usar
Rode /fork seguido da tarefa para a cópia começar logo, ou só /fork para deixá-la esperando na visão de agentes.

Parâmetro opcional: [prompt]. Tarefa que a cópia começa a executar assim que for criada.

## Quando usar
Quando uma tarefa paralela pode rodar em segundo plano enquanto você segue com a conversa atual.

## Observação
Documentado na referência oficial. Com a visão de agentes desligada, o /fork inicia um subagente bifurcado. Para entregar uma tarefa lateral a um subagente cujo resultado volta a esta conversa, a referência indica /subtask.

## O que acontece no fluxo do prompt e do motor
1. Você digita /fork.
2. O motor copia a conversa.
3. A cópia roda em segundo plano.
4. Você segue na conversa atual.

## Exemplos
- /fork revise o módulo de pagamentos sem mexer no restante: a cópia começa esse trabalho em segundo plano enquanto você segue aqui.
- /fork: a cópia fica esperando o primeiro prompt na visão de agentes.
- /fork teste a migração do banco num worktree separado: a cópia trabalha no teste enquanto a conversa atual continua.

## Comandos relacionados
- /subtask: entrega tarefa lateral com retorno.

## Armadilhas
- Sem visão de agentes, vira subagente.
- Nada da cópia volta sozinho.

Documentação: https://code.claude.com/docs/en/agent-view#copy-the-session-with-%2Ffork
