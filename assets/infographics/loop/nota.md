# /loop: descrição completa

Categoria: Automação. Tipo: skill embutida do Claude Code. Alias: /proactive.

## O que faz
Roda um prompt ou um comando de barra repetidamente, num intervalo fixo ou no ritmo que o Claude escolher.

## Por que usar
Bom para acompanhar algo que demora, como um deploy ou uma fila, sem você precisar pedir de novo a cada vez.

## Como usar
Use /loop [intervalo] [prompt].

Parâmetros:
- [intervalo]: opcional. Tempo entre as voltas, como 5m ou 1h. Sem intervalo, o Claude decide quando voltar.
- [prompt]: o pedido ou o comando de barra que vai se repetir.

## Quando usar
Para acompanhar algo que demora, como um deploy ou uma fila, sem pedir de novo a cada vez.

## Observação
Não serve para tarefas de uma vez só. Para parar, peça na conversa que encerre o loop.
Serve para repetir dentro da sessão. As tarefas agendadas do Desktop são outro recurso.

## O que acontece no fluxo do prompt e do motor
1. Você digita /loop com o prompt.
2. O Claude roda o prompt.
3. O Claude espera o intervalo ou decide quando voltar.
4. O loop repete até você pedir para encerrar.
5. Você acompanha sem novo pedido.

## Exemplos
- /loop 10m confira se o deploy de staging terminou: repete a cada 10 minutos.
- /loop 1h /usage: acompanha o consumo do plano de hora em hora.
- /loop /recap: sem intervalo, o Claude escolhe o ritmo.

## Comandos relacionados
- /usage: acompanha o consumo do plano.
- /recap: repete o resumo sem intervalo.

## Armadilhas
- Não serve para tarefa única.
- Para parar, peça na conversa.

Documentação: https://code.claude.com/docs/en/scheduled-tasks
