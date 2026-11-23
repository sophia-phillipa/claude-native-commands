# /subtask: descrição completa

Categoria: Automação. Tipo: comando embutido do Claude Code.

## O que faz
Cria um subagente em segundo plano que herda a conversa inteira, trabalha na tarefa enquanto você segue e devolve o resultado para esta conversa.

## Por que usar
Serve para tarefas laterais que precisam de todo o contexto da conversa, sem parar o que você está fazendo.

## Como usar
Digite /subtask seguido da tarefa. Para copiar a conversa numa sessão separada em segundo plano, use /fork.

Parâmetro obrigatório: <task>, a tarefa que o subagente deve executar.

## Quando usar
Quando você quer uma tarefa lateral que precisa do contexto da conversa, em paralelo ao trabalho principal.

## Observação
Documentado na referência oficial: /subtask <task> cria um subagente bifurcado em segundo plano que herda a conversa inteira.

## O que acontece no fluxo do prompt e do motor
1. Você digita /subtask.
2. O subagente herda a conversa inteira.
3. Ele trabalha em segundo plano enquanto você segue na conversa.
4. O resultado volta à conversa.

## Exemplos
- /subtask revisar os testes do módulo de pagamento: cria um subagente que herda a conversa e devolve o resultado quando termina.
- /subtask levantar os endpoints sem documentação: a tarefa segue em segundo plano enquanto você continua na conversa.
- /fork: para copiar a conversa numa sessão separada, use /fork.

## Comandos relacionados
- /fork: copia a conversa numa sessão separada.

## Armadilhas
- Com a visão de agentes desligada, o comando não existe; o caminho é /fork.
- Só o resultado final volta à conversa; as chamadas de ferramenta do subagente ficam fora dela.

Documentação: https://code.claude.com/docs/en/sub-agents#fork-the-current-conversation
